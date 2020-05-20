"""users routes"""
from flask import current_app as app, jsonify, request
from models import TrainingBehaviour, BaseObject


@app.route('/training_behaviour/<user_id>', methods=['POST', 'GET'])

def create_training_behaviour(user_id):
    
    content                         = request.json        
    trainingbehaviour               = TrainingBehaviour()

    trainingbehaviour.UserNo                = int(user_id)
    trainingbehaviour.SumPassed             = str(content['SumPassed'])
    trainingbehaviour.InitialSamplesSize    = str(content['InitialSamplesSize'])
    trainingbehaviour.ReactionTimes         = str(content['ReactionTimes'])
    trainingbehaviour.ChoicesSize           = str(content['ChoicesSize'])
    trainingbehaviour.ChoicesCorrect        = str(content['ChoicesCorrect'])
    trainingbehaviour.Chosen                = str(content['Chosen'])
    trainingbehaviour.CorrectAns            = str(content['CorrectAns'])
    trainingbehaviour.NumTraining           = str(content['NumTraining'])

     
    BaseObject.check_and_save(trainingbehaviour)

    result = dict({"success": "yes"}) 
    
    return jsonify(result)