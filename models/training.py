"""User model"""
from sqlalchemy import Column, Integer

from models.db import Model
from models.base_object import BaseObject


class Training(BaseObject, Model):
    
    id = Column(Integer, primary_key=True)
       
    TrainingNo           = Column(Integer)
    TrialNo              = Column(Integer)
               
    InitialSample1Size   = Column(Integer)
    InitialSample2Size   = Column(Integer)
    InitialSample3Size   = Column(Integer)
   
    Choice1Size          = Column(Integer)
    Choice2Size          = Column(Integer)
    Choice1Correct       = Column(Integer)
    Choice2Correct       = Column(Integer)
    
    def get_id(self):
        return str(self.id)
    
    def get_training_no(self):
        return str(self.TrainingNo)
    
    def get_trial_no(self):
        return str(self.TrialNo)
    
    def get_initial_samples_size(self):
        tmp = [];
        tmp.append(self.InitialSample1Size) 
        tmp.append(self.InitialSample2Size)
        tmp.append(self.InitialSample3Size) 
        return (tmp) 
    
    def get_choices_size(self):
        tmp = [];
        tmp.append(self.Choice1Size) 
        tmp.append(self.Choice2Size)
        return (tmp) 
    
    def get_choices_correct(self):
        tmp = [];
        tmp.append(self.Choice1Correct) 
        tmp.append(self.Choice2Correct)
        return (tmp) 

    def errors(self):
        errors = super(Training, self).errors()
        return errors