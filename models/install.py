""" install """
from sqlalchemy import orm
from models.db import db


def install_models():
    print("its at the install stage")
    orm.configure_mappers()
    db.create_all()
    db.session.commit()
    