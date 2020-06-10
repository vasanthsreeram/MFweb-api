"""users routes"""
from flask import current_app as app, jsonify, request
from models import QuestionsBehaviour, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route("/questions_behaviour/last_user_no", methods=["GET"])
def get_last_participant_id():

    query  = db.db.session.query(func.max(QuestionsBehaviour.UserNo)).first_or_404()

    if query[0] is not None:
        result = dict({"new_user_no": str(int(query[0]) + 1)})
    else:
        result = dict({"new_user_no": str(1)})

    app.logger.info(result)
    return jsonify(result)

@app.route('/questions_behaviour/<user_id>', methods=['POST', 'GET'])

def create_questions_behaviour(user_id):
    
    content                          = request.json        
    questionsbehaviour               = QuestionsBehaviour()

    questionsbehaviour.UserNo                = int(user_id)
    questionsbehaviour.ProlificID            = str(content['ProlificID'])
    questionsbehaviour.UserStartTime         = str(content['UserStartTime'])
    questionsbehaviour.InstructionsStartTime = str(content['InstructionsStartTime'])
    questionsbehaviour.QuestionsStartTime    = str(content['QuestionsStartTime'])
    questionsbehaviour.QuestionsFinishTime   = str(content['QuestionsFinishTime'])
    questionsbehaviour.SumPassed             = str(content['SumPassed'])
    questionsbehaviour.PressedKeys           = str(content['PressedKeys'])
    questionsbehaviour.PercentagePassed      = str(content['PercentagePassed'])
    questionsbehaviour.ReactionTimes         = str(content['ReactionTimes'])
    questionsbehaviour.Correct               = str(content['Correct'])

     
    BaseObject.check_and_save(questionsbehaviour)

    result = dict({"success": "yes"}) 
    
    return jsonify(result)