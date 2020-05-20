"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime, Float, VARCHAR

from models.db import Model
from models.base_object import BaseObject


class Task(BaseObject, Model):
    
    id = Column(Integer, primary_key=True)
       
    UserNo               = Column(Integer)
    TrialNo              = Column(Integer)
    BlockNo              = Column(Integer)
    Horizon              = Column(Integer)
    ItemNo               = Column(Integer)
    InitialSampleNb      = Column(Integer)
    UnusedTree           = Column(Integer)
               
    InitialSample1Tree   = Column(Integer)
    InitialSample2Tree   = Column(Integer)
    InitialSample3Tree   = Column(Integer)
    InitialSample4Tree   = Column(Integer)
    InitialSample5Tree   = Column(Integer)
   
    InitialSample1Size   = Column(Integer)
    InitialSample2Size   = Column(Integer)
    InitialSample3Size   = Column(Integer)
    InitialSample4Size   = Column(Integer)
    InitialSample5Size   = Column(Integer)
   
    Tree1FutureSize1     = Column(Integer)
    Tree1FutureSize2     = Column(Integer)
    Tree1FutureSize3     = Column(Integer)
    Tree1FutureSize4     = Column(Integer)
    Tree1FutureSize5     = Column(Integer)
    Tree1FutureSize6     = Column(Integer)
   
    Tree2FutureSize1     = Column(Integer)
    Tree2FutureSize2     = Column(Integer)
    Tree2FutureSize3     = Column(Integer)
    Tree2FutureSize4     = Column(Integer)
    Tree2FutureSize5     = Column(Integer)
    Tree2FutureSize6     = Column(Integer)
    
    Tree3FutureSize1     = Column(Integer)
    Tree3FutureSize2     = Column(Integer)
    Tree3FutureSize3     = Column(Integer)
    Tree3FutureSize4     = Column(Integer)
    Tree3FutureSize5     = Column(Integer)
    Tree3FutureSize6     = Column(Integer)
   
    Tree4FutureSize1     = Column(Integer)
    Tree4FutureSize2     = Column(Integer)
    Tree4FutureSize3     = Column(Integer)
    Tree4FutureSize4     = Column(Integer)
    Tree4FutureSize5     = Column(Integer)
    Tree4FutureSize6     = Column(Integer)
    
    
    def get_id(self):
        return str(self.id)
    
    def get_user_no(self):
        return str(self.UserNo)
    
    def get_trial_no(self):
        return str(self.TrialNo)
    
    def get_block_no(self):
        return str(self.BlockNo)
    
    def get_horizon(self):
        return str(self.Horizon)
    
    def get_item_no(self):
        return str(self.ItemNo)
    
    def get_initial_sample_nb(self):
        return str(self.InitialSampleNb)
    
    def get_unused_tree(self):
        return str(self.UnusedTree)
    
    
    def get_sample_1_tree(self):
        return (str(self.InitialSample1Tree)+(',')+str(self.InitialSample2Tree))
  
    def get_sample_2_tree(self):
        return str(self.InitialSample2Tree)
    
    def get_sample_3_tree(self):
        return str(self.InitialSample3Tree)
    
    def get_sample_4_tree(self):
        return str(self.InitialSample4Tree)
    
    def get_sample_5_tree(self):
        return str(self.InitialSample5Tree)
    
    
    def get_sample_1_size(self):
        return str(self.InitialSample1Size)
    
    def get_sample_2_size(self):
        return str(self.InitialSample2Size)
   
    def get_sample_3_size (self):
        return str(self.InitialSample3Size)
    
    def get_sample_4_size (self):
        return str(self.InitialSample4Size)
    
    def get_sample_5_size(self):
        return str(self.InitialSample5Size)
    
    
    def get_tree1_future_size_1(self):
        return str(self.Tree1FutureSize1)
    
    def get_tree1_future_size_2(self):
        return str(self.Tree1FutureSize2)
    
    def get_tree1_future_size_3(self):
        return str(self.Tree1FutureSize3)
    
    def get_tree1_future_size_4(self):
        return str(self.Tree1FutureSize4)
    
    def get_tree1_future_size_5(self):
        return str(self.Tree1FutureSize5)
        
    def get_tree1_future_size_6(self):
        return str(self.Tree1FutureSize6)
    
    
    def get_tree2_future_size_1(self):
        return str(self.Tree2FutureSize1)
        
    def get_tree2_future_size_2(self):
        return str(self.Tree2FutureSize2)
    
    def get_tree2_future_size_3(self):
        return str(self.Tree2FutureSize3)
    
    def get_tree2_future_size_4(self):
        return str(self.Tree2FutureSize4)
    
    def get_tree2_future_size_5(self):
        return str(self.Tree2FutureSize5)
    
    def get_tree2_future_size_6(self):
        return str(self.Tree2FutureSize6)
    
    
    def get_tree3_future_size_1(self):
        return str(self.Tree3FutureSize1)
    
    def get_tree3_future_size_2(self):
        return str(self.Tree3FutureSize2)
   
    def get_tree3_future_size_3(self):
        return str(self.Tree3FutureSize3)
    
    def get_tree3_future_size_4(self):
        return str(self.Tree3FutureSize4)
    
    def get_tree3_future_size_5(self):
        return str(self.Tree3FutureSize5)
    
    def get_tree3_future_size_6(self):
        return str(self.Tree3FutureSize6)
    
    
    def get_tree4_future_size_1(self):
        return str(self.Tree4FutureSize1)
   
    def get_tree4_future_size_2(self):
        return str(self.Tree4FutureSize2)
    
    def get_tree4_future_size_3(self):
        return str(self.Tree4FutureSize3)
    
    def get_tree4_future_size_4(self):
        return str(self.Tree4FutureSize4)
        
    def get_tree4_future_size_5(self):
        return str(self.Tree4FutureSize5)
    
    def get_tree4_future_size_6(self):
        return str(self.Tree4FutureSize6)

    

    def errors(self):
        errors = super(Trial, self).errors()
        return errors