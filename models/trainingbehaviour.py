"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class TrainingBehaviour(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    UserNo              = Column(Integer)
    ProlificID          = Column(Text)
    TrainingNo          = Column(Text)
    TaskNo              = Column(Text)
    Date                = Column(Text)
    UserStartTime       = Column(Text)
    TrainingStartTime   = Column(Text)
    TrainingFinishTime  = Column(Text)
    SumPassed           = Column(Text)
    ChoicesSize         = Column(Text)
    InitialSamplesSize  = Column(Text)
    ReactionTimes       = Column(Text)
    ChoicesCorrect      = Column(Text)
    Chosen              = Column(Text)
    CorrectAns          = Column(Text)
    NumTraining         = Column(Text)


    def get_id(self):
        return str(self.id)

    def get_prolific_id(self):
        return str(self.ProlificID)

    def get_task_player_id(self):
        return str(self.TaskNo)

    def get_training_player_id(self):
        return str(self.TrainingNo)

    def get_date(self):
        return str(self.Date)

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
