""" db """
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
print("db has been init")
Model = db.Model