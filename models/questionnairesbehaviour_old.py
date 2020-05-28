"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class QuestionnairesBehaviour(BaseObject, Model):
    
    id = Column(Integer, primary_key=True)
       
    UserNo              = Column(Integer)
    PageNo0             = Column(Text(length=10000))
    PageNo1             = Column(Text(length=10000))
    PageNo2             = Column(Text(length=10000))
    PageNo3             = Column(Text(length=10000))
    PageNo4             = Column(Text(length=10000))
    PageNo5             = Column(Text(length=10000))
    IQ_1             = Column(Text(length=10000))
    IQ_2             = Column(Text(length=10000))
    IQ_3             = Column(Text(length=10000))
    IQ_4             = Column(Text(length=10000))
    IQ_5             = Column(Text(length=10000))
    IQ_6             = Column(Text(length=10000))
    IQ_7             = Column(Text(length=10000))
    IQ_8             = Column(Text(length=10000))
    
    def get_id(self):
        return str(self.id)
    
    def get_user_no(self):
        return str(self.UserNo)
    
    def get_page_no_0(self):
        return str(self.PageNo0)
    
    def get_page_no_1(self):
        return str(self.PageNo1)
    
    def get_page_no_2(self):
        return str(self.PageNo2)
    
    def get_page_no_3(self):
        return str(self.PageNo3)
    
    def get_page_no_4(self):
        return str(self.PageNo4)
    
    def get_page_no_5(self):
        return str(self.PageNo5)
    
    def get_iq_1(self):
        return str(self.IQ_1)
    
    def get_iq_2(self):
        return str(self.IQ_2)
    
    def get_iq_3(self):
        return str(self.IQ_3)
    
    def get_iq_4(self):
        return str(self.IQ_4)
    
    def get_iq_5(self):
        return str(self.IQ_5)
    
    def get_iq_6(self):
        return str(self.IQ_6)
    
    def get_iq_7(self):
        return str(self.IQ_7)
    
    def get_iq_8(self):
        return str(self.IQ_8)

    def errors(self):
        errors = super(QuestionnairesBehaviour, self).errors()
        return errors