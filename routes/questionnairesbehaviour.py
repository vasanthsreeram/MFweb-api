"""users routes"""
from flask import current_app as app, jsonify, request
from models import QuestionnairesBehaviour, BaseObject, db
from sqlalchemy.sql.expression import func


@app.route('/questionnaires_behaviour/<user_id>', methods=['POST', 'GET'])

def create_questionnaires_behaviour(user_id):

    content                               = request.json
    questionnairesbehaviour               = QuestionnairesBehaviour()

    questionnairesbehaviour.UserNo          = int(user_id)
    questionnairesbehaviour.ProlificID      = str(content['ProlificID'])
    questionnairesbehaviour.UserStartTime   = str(content['UserStartTime'])

    questionnairesbehaviour.Date                         = str(content['Date'])
    questionnairesbehaviour.QuestionnaireStartTime       = str(content['QuestionnaireStartTime'])
    questionnairesbehaviour.QuestionnaireFinishTime      = str(content['QuestionnaireFinishTime'])

    questionnairesbehaviour.PageNo0         = str(content['PageNo0'])
    questionnairesbehaviour.PageNo1         = str(content['PageNo1'])
    questionnairesbehaviour.PageNo2         = str(content['PageNo2'])
    questionnairesbehaviour.PageNo3         = str(content['PageNo3'])
    questionnairesbehaviour.PageNo4         = str(content['PageNo4'])
    questionnairesbehaviour.PageNo5         = str(content['PageNo5'])

    questionnairesbehaviour.IQ_1            = str(content['IQ_1'])
    questionnairesbehaviour.IQ_2            = str(content['IQ_2'])
    questionnairesbehaviour.IQ_3            = str(content['IQ_3'])
    questionnairesbehaviour.IQ_4            = str(content['IQ_4'])
    questionnairesbehaviour.IQ_5            = str(content['IQ_5'])
    questionnairesbehaviour.IQ_6            = str(content['IQ_6'])
    questionnairesbehaviour.IQ_7            = str(content['IQ_7'])
    questionnairesbehaviour.IQ_8            = str(content['IQ_8'])

    questionnairesbehaviour.IQimage_1            = str(content['IQimage_1'])
    questionnairesbehaviour.IQimage_2            = str(content['IQimage_2'])
    questionnairesbehaviour.IQimage_3            = str(content['IQimage_3'])
    questionnairesbehaviour.IQimage_4            = str(content['IQimage_4'])
    questionnairesbehaviour.IQimage_5            = str(content['IQimage_5'])
    questionnairesbehaviour.IQimage_6            = str(content['IQimage_6'])
    questionnairesbehaviour.IQimage_7            = str(content['IQimage_7'])
    questionnairesbehaviour.IQimage_8            = str(content['IQimage_8'])

    questionnairesbehaviour.ASRS             = str(content['ASRS'])
    questionnairesbehaviour.BIS11            = str(content['BIS11'])
    questionnairesbehaviour.IUS              = str(content['IUS'])
    questionnairesbehaviour.LSAS             = str(content['LSAS'])
    questionnairesbehaviour.SDS              = str(content['SDS'])
    questionnairesbehaviour.STAI             = str(content['STAI'])

    BaseObject.check_and_save(questionnairesbehaviour)

    result = dict({"success": "yes"})

    return jsonify(result)
