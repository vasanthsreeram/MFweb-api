"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class Behaviour(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    UserNo                = Column(Integer)
    ProlificID            = Column(Text(length=10000))
    TaskNo                = Column(Text(length=10000))
    TrainingNo            = Column(Text(length=10000))
    UserStartTime         = Column(Text(length=10000))
    BlockNo               = Column(Integer)
    InfoRequestNo         = Column(Text(length=10000))
    BlockStartTime        = Column(Text(length=10000))
    BlockFinishTime       = Column(Text(length=10000))
    TreeColours           = Column(Text(length=10000))
    ChosenTree            = Column(Text(length=10000))
    ChosenAppleSize       = Column(Text(length=10000))
    AllKeyPressed         = Column(Text(length=10000))
    ReactionTimes         = Column(Text(length=10000))
    Horizon               = Column(Text(length=10000))
    ItemNo                = Column(Text(length=10000))
    TrialNo               = Column(Text(length=10000))
    UnusedTree            = Column(Text(length=10000))
    InitialSamplesNb      = Column(Text(length=10000))
    InitialSamplesTree    = Column(Text(length=10000))
    InitialSamplesSize    = Column(Text(length=10000))
    TreePositions         = Column(Text(length=10000))


    def get_id(self):
        return str(self.id)

    def get_user_no(self):
        return str(self.UserNo)

    def get_task_info_request_no(self):
        return str(self.InfoRequestNo)
    
    def get_task_player_id(self):
        return str(self.TaskNo)

    def get_training_player_id(self):
        return str(self.TrainingNo)

    def get_prolific_id(self):
        return str(self.ProlificID)

    def get_user_start_time(self):
        return str(self.UserStartTime)

    def get_start_time(self):
        return str(self.BlockStartTime)

    def get_finish_time(self):
        return str(self.BlockFinishTime)

    def get_block_no(self):
        return str(self.BlockNo)

    def get_tree_colours(self):
        return str(self.TreeColours)

    def get_chosen_tree(self):
        return str(self.ChosenTree)

    def get_chosen_apple_size(self):
        return str(self.ChosenAppleSize)

    def get_all_key_pressed(self):
        return str(self.AllKeyPressed)

    def get_reaction_times(self):
        return str(self.ReactionTimes)

    def get_all_horizon(self):
        return str(self.Horizon)

    def get_all_item_no(self):
        return str(self.ItemNo)

    def get_all_trial_no(self):
        return str(self.TrialNo)

    def get_all_unused_tree(self):
        return str(self.UnusedTree)

    def get_all_initial_samples_nb(self):
        return str(self.InitialSamplesNb)

    def get_all_initial_samples_tree(self):
        return str(self.InitialSamplesTree)

    def get_all_initial_samples_size(self):
        return str(self.InitialSamplesSize)

    def get_all_tree_positions(self):
        return str(self.TreePositions)

    def errors(self):
        errors = super(Behaviour, self).errors()
        return errors
