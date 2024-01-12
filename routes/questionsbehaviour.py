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
    questionsbehaviour = QuestionsBehaviour(
        UserNo=int(user_id),
        ProlificID=str(content.get('ProlificID', '')),
        TrainingNo=str(content.get('TrainingNo', '')),
        TaskNo=str(content.get('TaskNo', '')),
        Date=str(content.get('Date', '')),
        UserStartTime=str(content.get('UserStartTime', '')),
        InstructionsStartTime=str(content.get('InstructionsStartTime', '')),
        QuestionsStartTime=str(content.get('QuestionsStartTime', '')),
        QuestionsFinishTime=str(content.get('QuestionsFinishTime', '')),
        SumPassed=str(content.get('SumPassed', '')),
        PressedKeys=str(content.get('PressedKeys', '')),
        PercentagePassed=str(content.get('PercentagePassed', '')),
        ReactionTimes=str(content.get('ReactionTimes', '')),
        Correct=str(content.get('Correct', ''))
    )


    BaseObject.check_and_save(questionsbehaviour)

    result = dict({"success": "yes"})

    return jsonify(result)
