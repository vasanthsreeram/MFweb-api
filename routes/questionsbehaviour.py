"""users routes"""
from flask import current_app as app, jsonify, request
from models import QuestionsBehaviour, BaseObject


@app.route('/questions_behaviour/<user_id>', methods=['POST', 'GET'])

def create_questions_behaviour(user_id):
    
    content                          = request.json        
    questionsbehaviour               = QuestionsBehaviour()

    questionsbehaviour.UserNo               = int(user_id)
    questionsbehaviour.SumPassed            = str(content['SumPassed'])
    questionsbehaviour.PressedKeys          = str(content['PressedKeys'])
    questionsbehaviour.PercentagePassed     = str(content['PercentagePassed'])
    questionsbehaviour.ReactionTimes        = str(content['ReactionTimes'])
    questionsbehaviour.Correct              = str(content['Correct'])

     
    BaseObject.check_and_save(questionsbehaviour)

    result = dict({"success": "yes"}) 
    
    return jsonify(result)