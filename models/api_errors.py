""" api errors """
# coding=utf-8
import json


class ApiErrors(Exception):
    def __init__(self):
        self.errors = {}

    def addError(self, field, error):
        if field not in self.errors:
            self.errors[field] = []
        self.errors[field].append(error)


    def checkDate(self, field, value):
        if (isinstance(value, str) or isinstance(value, str)) and re.search('^\d{4}-\d{2}-\d{2}( \d{2}:\d{2}(:\d{2})?)?$', value):
            return True
        else:
            self.addError(field, 'Format de date incorrect')

    def checkFloat(self, field, value):
        if isinstance(value, float) or \
           ((isinstance(value, str) or isinstance(value, str)) and re.search('^\d+(\.\d*|)$', value)):
            return True
        else:
            self.addError(field, 'La valeur doit etre un nombre (optionnellement a virgule).')

    def checkWithin(self, field, value, min, max):
        self.checkUnder(field, value, max)
        self.checkOver(field, value, min)

    def checkOver(self, field, value, min):
        if value>min:
            return True
        else:
            self.addError(field, 'La valeur doit etre superieure a '+str(min))

    def checkUnder(self, field, value, max):
        if value<min:
            return True
        else:
            self.addError(field, 'La valeur doit etre inferieure a '+str(min))

    def checkMinLength(self, field, value, length):
        if len(value)<length:
            self.addError(field, 'Vous devez saisir au moins '+str(length)+' caracteres.')

    def checkEmail(self, field, value):
        if not "@" in value:
            self.addError(field, 'L''e-mail doit contenir un @.')

    def maybeRaise(self):
        if len(self.errors)>0:
            raise self

    def __str__(self):
        if self.errors:
            return json.dumps(self.errors, indent=2)

    status_code = None