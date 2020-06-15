"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime, Float, VARCHAR

from models.db import Model
from models.base_object import BaseObject


class Task(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    TaskNo               = Column(Integer)
    TrialNo              = Column(Integer)
    BlockNo              = Column(Integer)
    Horizon              = Column(Integer)
    ItemNo               = Column(Integer)
    InitialSampleNb      = Column(Integer)
    UnusedTree           = Column(Integer)

    DisplayOrder1        = Column(Integer)
    DisplayOrder2        = Column(Integer)
    DisplayOrder3        = Column(Integer)

    TreePositions1       = Column(Integer)
    TreePositions2       = Column(Integer)
    TreePositions3       = Column(Integer)
    TreePositions4       = Column(Integer)

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

    def get_task_no(self):
        return str(self.TaskNo)

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

    def get_display_order(self):
        tmp = [];
        tmp.append(self.DisplayOrder1)
        tmp.append(self.DisplayOrder2)
        tmp.append(self.DisplayOrder3)
        return (tmp)

    def get_tree_positions(self):
        tmp = [];
        tmp.append(self.TreePositions1)
        tmp.append(self.TreePositions2)
        tmp.append(self.TreePositions3)
        tmp.append(self.TreePositions4)
        return (tmp)

    def get_initial_samples_tree(self):
        tmp = [];
        tmp.append(self.InitialSample1Tree)
        tmp.append(self.InitialSample2Tree)
        tmp.append(self.InitialSample3Tree)
        tmp.append(self.InitialSample4Tree)
        tmp.append(self.InitialSample5Tree)
        return (tmp)

    def get_initial_samples_size(self):
        tmp = [];
        tmp.append(self.InitialSample1Size)
        tmp.append(self.InitialSample2Size)
        tmp.append(self.InitialSample3Size)
        tmp.append(self.InitialSample4Size)
        tmp.append(self.InitialSample5Size)
        return (tmp)

    def get_tree1_future_size(self):
        tmp = [];
        tmp.append(self.Tree1FutureSize1)
        tmp.append(self.Tree1FutureSize2)
        tmp.append(self.Tree1FutureSize3)
        tmp.append(self.Tree1FutureSize4)
        tmp.append(self.Tree1FutureSize5)
        tmp.append(self.Tree1FutureSize6)
        return (tmp)

    def get_tree2_future_size(self):
        tmp = [];
        tmp.append(self.Tree2FutureSize1)
        tmp.append(self.Tree2FutureSize2)
        tmp.append(self.Tree2FutureSize3)
        tmp.append(self.Tree2FutureSize4)
        tmp.append(self.Tree2FutureSize5)
        tmp.append(self.Tree2FutureSize6)
        return (tmp)

    def get_tree3_future_size(self):
        tmp = [];
        tmp.append(self.Tree3FutureSize1)
        tmp.append(self.Tree3FutureSize2)
        tmp.append(self.Tree3FutureSize3)
        tmp.append(self.Tree3FutureSize4)
        tmp.append(self.Tree3FutureSize5)
        tmp.append(self.Tree3FutureSize6)
        return (tmp)

    def get_tree4_future_size(self):
        tmp = [];
        tmp.append(self.Tree4FutureSize1)
        tmp.append(self.Tree4FutureSize2)
        tmp.append(self.Tree4FutureSize3)
        tmp.append(self.Tree4FutureSize4)
        tmp.append(self.Tree4FutureSize5)
        tmp.append(self.Tree4FutureSize6)
        return (tmp)


    def errors(self):
        errors = super(Task, self).errors()
        return errors
