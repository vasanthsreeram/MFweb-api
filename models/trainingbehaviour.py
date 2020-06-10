"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class TrainingBehaviour(BaseObject, Model):
    
    id = Column(Integer, primary_key=True)
       
    UserNo              = Column(Integer)
    ProlificID      = Column(Text(length=10000))
    UserStartTime       = Column(Text(length=10000))
    TrainingStartTime   = Column(Text(length=10000))
    TrainingFinishTime  = Column(Text(length=10000))
    SumPassed           = Column(Text(length=10000))
    ChoicesSize         = Column(Text(length=10000))
    InitialSamplesSize  = Column(Text(length=10000)) 
    ReactionTimes       = Column(Text(length=10000))
    ChoicesCorrect      = Column(Text(length=10000))
    Chosen              = Column(Text(length=10000))
    CorrectAns          = Column(Text(length=10000))
    NumTraining         = Column(Text(length=10000))

    
    def get_id(self):
        return str(self.id)
    
    def get_prolific_id(self):
        return str(self.ProlificID)
    
    def get_user_start_time(self):
        return str(self.UserStartTime)
    
    def get_user_no(self):
        return str(self.UserNo)
    
    def get_training_start_time(self):
        return str(self.TrainingStartTime)
    
    def get_training_finish_time(self):
        return str(self.TrainingFinishTime)
    
    def get_sum_passed(self):
        return str(self.SumPassed)
    
    def get_choices_size(self):
        return str(self.ChoicesSize)
        
    def get_choices_correct(self):
        return str(self.ChoicesCorrect)
    
    def get_reaction_times(self):
        return str(self.ReactionTimes)
    
    def get_initial_samples_size(self):
        return str(self.InitialSamplesSize)
        
    def get_chosen(self):
        return str(self.Chosen)
        
    def get_correct_ans(self):
        return str(self.CorrectAns)
        
    def get_num_training(self):
        return str(self.NumTraining)

    def errors(self):
        errors = super(TrainingBehaviour, self).errors()
        return errors