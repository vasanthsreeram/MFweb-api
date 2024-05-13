"""users routes"""
from flask import current_app as app, jsonify, request
from models import TrainingBehaviour, BaseObject

@app.route('/training_behaviour/<user_id>', methods=['POST', 'GET'])
def create_training_behaviour(user_id):
    content = request.json
    print("traning behaviour", user_id)
    print("traning content", content)

    trainingbehaviour = TrainingBehaviour()

    # trainingbehaviour.UserNo = int(user_id)
    # trainingbehaviour.UserStartTime = content.get('UserStartTime', '')
    # trainingbehaviour.ProlificID = content.get('ProlificID', '')
    # trainingbehaviour.TrainingNo = content.get('TrainingNo', '')
    # trainingbehaviour.TaskNo = content.get('TaskNo', '')
    # trainingbehaviour.Date = content.get('Date', '')
    # trainingbehaviour.TrainingStartTime = content.get('TrainingStartTime', '')
    # trainingbehaviour.TrainingFinishTime = content.get('TrainingFinishTime', '')
    # trainingbehaviour.SumPassed = content.get('SumPassed', '')
    # trainingbehaviour.InitialSamplesSize = content.get('InitialSamplesSize', '')
    # trainingbehaviour.ReactionTimes = content.get('ReactionTimes', '')
    # trainingbehaviour.ChoicesSize = content.get('ChoicesSize', '')
    # trainingbehaviour.ChoicesCorrect = content.get('ChoicesCorrect', '')
    # trainingbehaviour.Chosen = content.get('Chosen', '')
    # trainingbehaviour.CorrectAns = content.get('CorrectAns', '')
    # trainingbehaviour.NumTraining = content.get('NumTraining', '')

    trainingbehaviour.UserNo = int(user_id)
    trainingbehaviour.UserStartTime = str(content.get('UserStartTime', ''))
    trainingbehaviour.ProlificID = str(content.get('ProlificID', ''))
    trainingbehaviour.TrainingNo = str(content.get('TrainingNo', ''))
    trainingbehaviour.TaskNo = str(content.get('TaskNo', ''))
    trainingbehaviour.Date = str(content.get('Date', ''))
    trainingbehaviour.TrainingStartTime = str(content.get('TrainingStartTime', ''))
    trainingbehaviour.TrainingFinishTime = str(content.get('TrainingFinishTime', ''))
    trainingbehaviour.SumPassed = str(content.get('SumPassed', ''))
    trainingbehaviour.InitialSamplesSize = str(content.get('InitialSamplesSize', ''))
    trainingbehaviour.ReactionTimes = str(content.get('ReactionTimes', ''))
    trainingbehaviour.ChoicesSize = str(content.get('ChoicesSize', ''))
    trainingbehaviour.ChoicesCorrect = str(content.get('ChoicesCorrect', ''))
    trainingbehaviour.Chosen = str(content.get('Chosen', ''))
    trainingbehaviour.CorrectAns = str(content.get('CorrectAns', ''))
    trainingbehaviour.NumTraining = str(content.get('NumTraining', ''))
    print("saving this ", trainingbehaviour)
    # BaseObject.check_and_save(trainingbehaviour)

    result = {"success": "yes"}

    return jsonify(result)
