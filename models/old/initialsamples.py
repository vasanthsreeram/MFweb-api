"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime, Float, VARCHAR

from models.db import Model
from models.base_object import BaseObject


class Initialsamples(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    ItemNo              = Column(Integer)
    UserNo              = Column(Integer)
    UnusedTree          = Column(Integer)
    SampleNo            = Column(Integer)    
    Tree                = Column(Integer)
    Size                = Column(Integer)
    
    
    def get_id(self):
        return str(self.id)
    
    def get_item_no(self):
        return str(self.ItemNo)
    
    def get_unused_tree(self):
        return str(self.UnusedTree)
    
    def get_sample_no(self):
        return str(self.SampleNo)     
        
    def get_user_no(self):
        return str(self.UserNo)   
        
    def get_tree(self):
        return str(self.Tree)
        
    def get_size(self):
        return str(self.Size)

    def errors(self):
        errors = super(InitialSamples, self).errors()
        return errors