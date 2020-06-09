"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class QuestionsBehaviour(BaseObject, Model):
    
    id = Column(Integer, primary_key=True)
       
    UserNo                = Column(Integer)
    UserStartTime         = Column(Text(length=10000))
    InstructionsStartTime = Column(Text(length=10000))
    QuestionsStartTime    = Column(Text(length=10000))
    QuestionsFinishTime   = Column(Text(length=10000))
    SumPassed             = Column(Text(length=10000))
    PressedKeys           = Column(Text(length=10000))
    PercentagePassed      = Column(Text(length=10000)) 
    ReactionTimes         = Column(Text(length=10000)) 
    Correct               = Column(Text(length=10000))


    def get_id(self):
        return str(self.id)
    
    def get_user_no(self):
        return str(self.UserNo)
    
    def get_user_start_time(self):
        return str(self.UserStartTime)
    
    def get_instructions_starttime(self):
        return str(self.InstructionsStartTime)
    
    def get_questions_starttime(self):
        return str(self.QuestionsStartTime)
    
    def get_questions_finishtime(self):
        return str(self.QuestionsFinishTime)
    
    def get_sum_passed(self):
        return str(self.SumPassed)
    
    def get_pressed_keys(self):
        return str(self.PressedKeys)
    
    def get_percentage_passed(self):
        return str(self.PercentagePassed)
    
    def get_reaction_times(self):
        return str(self.ReactionTimes)
    
    def get_correct(self):
        return str(self.Correct)

    def errors(self):
        errors = super(QuestionsBehaviour, self).errors()
        return errors