"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime, Float, VARCHAR

from models.db import Model
from models.base_object import BaseObject


class Trial(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    TaskID            = Column(Integer)
    UserNo            = Column(Integer)
    ItemNo            = Column(Integer)
    Horizon           = Column(Integer)
    BlockNo           = Column(Integer)
    TrialNo           = Column(Integer)
    SampleNb          = Column(Integer)
    
    
    def get_id(self):
        return str(self.id)
    
    def get_task_id(self):
        return str(self.TaskID)
    
    def get_user_no(self):
        return str(self.UserNo)
        
    def get_item_no(self):
        return str(self.ItemNo)
        
    def get_horizon(self):
        return str(self.Horizon)
        
    def get_block_no(self):
        return str(self.BlockNo)
    
    def get_trial_no(self):
        return str(self.TrialNo)
    
    def get_sample_nb(self):
        return str(self.SampleNb)

    def errors(self):
        errors = super(Trial, self).errors()
        return errors