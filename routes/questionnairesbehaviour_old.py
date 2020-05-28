"""users routes"""
from flask import current_app as app, jsonify, request
from models import QuestionnairesBehaviour, BaseObject


@app.route('/questionnaires_behaviour/<user_id>', methods=['POST', 'GET'])

def create_questionnaires_behaviour(user_id):
    
    content                               = request.json        
    questionnairesbehaviour               = QuestionnairesBehaviour()

    questionnairesbehaviour.PageNo0 = str(content['PageNo0'])
    questionnairesbehaviour.PageNo1 = str(content['PageNo1'])
    questionnairesbehaviour.PageNo2 = str(content['PageNo2'])      
    questionnairesbehaviour.PageNo3 = str(content['PageNo3'])        
    questionnairesbehaviour.PageNo4 = str(content['PageNo4'])         
    questionnairesbehaviour.PageNo5 = str(content['PageNo5'])
    questionnairesbehaviour.IQ_1 = str(content['IQ_1'])
    questionnairesbehaviour.IQ_2 = str(content['IQ_2'])
    questionnairesbehaviour.IQ_3 = str(content['IQ_3'])
    questionnairesbehaviour.IQ_4 = str(content['IQ_4'])
    questionnairesbehaviour.IQ_5 = str(content['IQ_5'])
    questionnairesbehaviour.IQ_6 = str(content['IQ_6'])
    questionnairesbehaviour.IQ_7 = str(content['IQ_7'])
    questionnairesbehaviour.IQ_8 = str(content['IQ_8'])

    BaseObject.check_and_save(questionnairesbehaviour)

    result = dict({"success": "yes"}) 
    
    return jsonify(result)