""" main_object """
from collections import OrderedDict
from datetime import datetime
from decimal import Decimal, InvalidOperation
from sqlalchemy.orm import declarative_base
from pprint import pprint
import re
from psycopg2.extras import DateTimeRange
from sqlalchemy import CHAR,\
                       BigInteger,\
                       Column,\
                       Enum,\
                       Float,\
                       Integer,\
                       Numeric,\
                       String
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.exc import DataError, IntegrityError
from sqlalchemy.inspection import inspect
import humanize
from models.api_errors import ApiErrors
from models.db import db
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import registry
from sqlalchemy import create_engine
from humanize import intword

username = "gridgame"
password = "J35pZyjo9kLQjh"
server = "clic.database.windows.net"
database = "clic"

db_uri = f"mssql+pymssql://{username}:{password}@{server}/{database}"

# Create the SQLAlchemy engine
engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)

DUPLICATE_KEY_ERROR_CODE = '23505'
NOT_FOUND_KEY_ERROR_CODE = '23503'
OBLIGATORY_FIELD_ERROR_CODE = '23502'

mapper_registry = registry()
Base = mapper_registry.generate_base()


def serialize(value, **options):
    if isinstance(value, Enum):
        return value.name
    elif isinstance(value, datetime):
        return value.isoformat() + "Z"
    elif isinstance(value, DateTimeRange):
        return {'start': value.lower, 'end': value.upper}
    elif isinstance(value, list) and value and isinstance(value[0], DateTimeRange):
        return [{'start': d.lower, 'end': d.upper} for d in value]
    else:
        return value

class BaseObject():
    id = Column(BigInteger,
                primary_key=True,
                autoincrement=True)

    def __init__(self, **options):
        if options and 'from_dict' in options and options['from_dict']:
            self.populateFromDict(options['from_dict'])

    def _asdict(self, **options):
        result = OrderedDict()
        for key in inspect(self.__class__).attrs.keys():
            if options and 'include' in options and "-" + key in options['include']:
                continue

            value = getattr(self, key)
            if options and 'cut' in options and isinstance(value, str) and len(value) > options['cut']:
                value = value[:options['cut']] + '...'

            if key == 'id' or key.endswith('Id'):
                result[key] = intword(value)
                if 'dehumanize' in options and options['dehumanize']:
                    result['dehumanized' + key[0].capitalize() + key[1:]] = value
            elif key != 'validationToken':
                if isinstance(value, InstrumentedList) or hasattr(value, '__table__'):
                    # Handling for relationships and models
                    sub_values = [item._asdict(**options) for item in value] if isinstance(value, list) else value._asdict(**options)
                    result[key] = sub_values
                else:
                    # Direct serialization
                    result[key] = serialize(value, **options)

        # Add model name
        result['modelName'] = self.__class__.__name__

        # Additional logic for included joins
        if options and 'include' in options and options['include']:
            for join in options['include']:
                if isinstance(join, str) and join.startswith('-'):
                    continue
                elif isinstance(join, dict):
                    key = join['key']
                    refine = join.get('refine')
                    resolve = join.get('resolve')
                    sub_joins = join.get('sub_joins')
                else:
                    key = join
                    refine = None
                    resolve = None
                    sub_joins = None
                try:
                    value = getattr(self, key)
                except AttributeError:
                    continue
                if callable(value):
                    value = value()
                if value is not None:
                    if isinstance(value, InstrumentedList) or hasattr(value, '__table__'):
                        if refine is None:
                            final_value = value
                        else:
                            final_value = refine(value, options.get('filters', {}))
                        final_value = [item._asdict(**options) for item in final_value if not item.is_soft_deleted()]
                        result[key] = final_value
                        if resolve:
                            result[key] = [resolve(v, options.get('filters', {})) for v in result[key]]
                    elif isinstance(value, BaseObject):
                        result[key] = value._asdict(include=sub_joins, cut=options.get('cut'))
                        if resolve:
                            result[key] = resolve(result[key], options.get('filters', {}))
                    else:
                        result[key] = serialize(value)

        if options and 'resolve' in options and options['resolve']:
            return options['resolve'](result, options.get('filters', {}))
        else:
            return result

    def dump(self):
        pprint(vars(self))

    def errors(self):
        errors = ApiErrors()
        columns = inspect(self.__class__).columns
        for key in columns.keys():
            col = columns[key]
            val = getattr(self, key)
            if not isinstance(col, Column):
                continue
            if not col.nullable and not col.foreign_keys and not col.primary_key and col.default is None and val is None:
                errors.addError(key, 'Cette information est obligatoire')
            if val is None:
                continue
            if isinstance(col.type, (String, CHAR)) and not isinstance(col.type, Enum) and not isinstance(val, str):
                errors.addError(key, 'doit etre une chaine de caracteres')
            if isinstance(col.type, (String, CHAR)) and isinstance(val, str) and col.type.length and len(val) > col.type.length:
                errors.addError(key, 'Vous devez saisir moins de ' + str(col.type.length) + ' caracteres')
            if isinstance(col.type, Integer) and not isinstance(val, int):
                errors.addError(key, 'doit etre un entier')
            if isinstance(col.type, Float) and not isinstance(val, float):
                errors.addError(key, 'doit etre un nombre')
        return errors

    def abortIfErrors(self):
        apiErrors = self.errors()
        if apiErrors.errors:
            raise apiErrors


    def abortIfErrors(self):
        apiErrors = self.errors()
        if apiErrors.errors:
            raise apiErrors

    @staticmethod
    def restize_global_error(e):
        logger.error("UNHANDLED ERROR : ")
        traceback.print_exc()
        return ["global", "Une erreur technique s'est produite. Elle a été notée, et nous allons investiguer au plus vite."]

    @staticmethod
    def restize_data_error(e):
        if e.args and len(e.args) > 0 and e.args[0].startswith('(psycopg2.DataError) value too long for type'):
            max_length = re.search('\(psycopg2.DataError\) value too long for type (.*?) varying\((.*?)\)', e.args[0], re.IGNORECASE).group(2)
            return ['global', "La valeur d'une entrée est trop longue (max " + max_length + ")"]
        else:
            return BaseObject.restize_global_error(e)

    @staticmethod
    def restize_integrity_error(e):
        if hasattr(e, 'orig') and hasattr(e.orig, 'pgcode') and e.orig.pgcode == DUPLICATE_KEY_ERROR_CODE:
            field = re.search('Key \((.*?)\)=', str(e._message), re.IGNORECASE).group(1)
            return [field, 'Une entrée avec cet identifiant existe déjà dans notre base de données']
        elif hasattr(e, 'orig') and hasattr(e.orig, 'pgcode') and e.orig.pgcode == NOT_FOUND_KEY_ERROR_CODE:
            field = re.search('Key \((.*?)\)=', str(e._message), re.IGNORECASE).group(1)
            return [field, 'Aucun objet ne correspond à cet identifiant dans notre base de données']
        elif hasattr(e, 'orig') and hasattr(e.orig, 'pgcode') and e.orig.pgcode == OBLIGATORY_FIELD_ERROR_CODE:
            field = re.search('column "(.*?)"', e.orig.pgerror, re.IGNORECASE).group(1)
            return [field, 'Ce champ est obligatoire']
        else:
            return BaseObject.restize_global_error(e)

    @staticmethod
    def restize_type_error(e):
        if e.args and len(e.args)>1 and e.args[1] == 'geography':
            return [e.args[2], 'doit etre une liste de nombre décimaux comme par exemple : [2.22, 3.22]']
        elif e.args and len(e.args)>1 and e.args[1] and e.args[1]=='decimal':
            return [e.args[2], 'doit être un nombre décimal']
        elif e.args and len(e.args)>1 and e.args[1] and e.args[1]=='integer':
            return [e.args[2], 'doit être un entier']
        else:
            return BaseObject.restize_global_error(e)

    @staticmethod
    def restize_value_error(e):
        if len(e.args)>1 and e.args[1] == 'enum':
            return [e.args[2], ' doit etre dans cette liste : '+",".join(map(lambda x : '"'+x+'"', e.args[3]))]
        else:
            return BaseObject.restize_global_error(e)      

    def populateFromDict(self, dct, skipped_keys=[]):
        data = dct.copy()
        if 'id' in data:
            del data['id']
        cols = inspect(self.__class__).columns
        for key in data:
            if key == 'deleted' or key in skipped_keys:
                continue

            if key in cols:
                col = cols[key]
                value = dehumanize(data[key]) if key.endswith('Id') else data[key]

                if isinstance(value, str):
                    if isinstance(col.type, Integer):
                        try:
                            setattr(self, key, int(value))
                        except ValueError:
                            raise TypeError('Invalid value for %s: %r' % (key, value), 'integer', key)
                    elif isinstance(col.type, (Float, Numeric)):
                        try:
                            setattr(self, key, float(value))
                        except ValueError:
                            raise TypeError('Invalid value for %s: %r' % (key, value), 'decimal', key)
                else:
                    setattr(self, key, value)

    @staticmethod
    def check_and_save(*objects):
        session = Session()
        if not objects:
            raise ValueError('Objects to save need to be passed as arguments'
                             + ' to check_and_save')

        # CUMULATE ERRORS IN ONE SINGLE API ERRORS DURING ADD TIME
        api_errors = ApiErrors()
        for obj in objects:
            obj_api_errors = obj.errors()
            if obj_api_errors.errors.keys():
                api_errors.errors.update(obj_api_errors.errors)
            else:
                session.add(obj)

        # CHECK BEFORE COMMIT
        if api_errors.errors.keys():
            raise api_errors

        # COMMIT
        try:
            print(session)
            return session.commit()
        except DataError as de:
            api_errors.addError(*BaseObject.restize_data_error(de))
            raise api_errors
        except IntegrityError as ie:
            api_errors.addError(*BaseObject.restize_integrity_error(ie))
            raise api_errors
        except TypeError as te:
            api_errors.addError(*BaseObject.restize_type_error(te))
            raise api_errors
        except ValueError as ve:
            api_errors.addError(*BaseObject.restize_value_error(ve))
            raise api_errors
        finally:
            session.close()
        if api_errors.errors.keys():
            raise api_errors
        

    @staticmethod
    def delete(model):
        db.session.delete(model)
        db.session.commit()

    def soft_delete(self):
        self.deleted = True
        db.session.add(self)

    def __repr__(self):
        id = "unsaved" \
            if self.id is None \
            else str(self.id) + "/" + intword(self.id)
        return '<%s #%s>' % (self.__class__.__name__,
                             id)
