"""users routes"""
from flask import current_app as app, jsonify, request
from models import QuestionnairesBehaviour, BaseObject, db
from sqlalchemy.sql.expression import func

print("inside qn behaviour route")

@app.route('/questionnaires_behaviour/<user_id>', methods=['POST', 'GET'])
def create_questionnaires_behaviour(user_id):
    content = request.json
    print("question behaviour conent", content)
    questionnairesbehaviour = QuestionnairesBehaviour(
        UserNo=int(user_id),
        ProlificID=str(content.get('ProlificID', '')),
        TrainingNo=str(content.get('TrainingNo', '')),
        TaskNo=str(content.get('TaskNo', '')),
        UserStartTime=str(content.get('UserStartTime', '')),
        Shuffle=str(content.get('Shuffle', '')),
        Date=str(content.get('Date', '')),
        QuestionnaireStartTime=str(content.get('QuestionnaireStartTime', '')),
        QuestionnaireFinishTime=str(content.get('QuestionnaireFinishTime', '')),
        PageNo0=str(content.get('PageNo0', '')),
        PageNo1=str(content.get('PageNo1', '')),
        PageNo2=str(content.get('PageNo2', '')),
        PageNo3=str(content.get('PageNo3', '')),
        PageNo4=str(content.get('PageNo4', '')),
        PageNo5=str(content.get('PageNo5', '')),
        PageNo6=str(content.get('PageNo6', '')),
        PageNo7=str(content.get('PageNo7', '')),
        PageNo8=str(content.get('PageNo8', '')),
        PageNo9=str(content.get('PageNo9', '')),
        PageNo10=str(content.get('PageNo10', '')),
        PageNo11=str(content.get('PageNo11', '')),
        PageNo12=str(content.get('PageNo12', '')),
        IQ_1=str(content.get('IQ_1', '')),
        IQ_2=str(content.get('IQ_2', '')),
        IQ_3=str(content.get('IQ_3', '')),
        IQ_4=str(content.get('IQ_4', '')),
        IQ_5=str(content.get('IQ_5', '')),
        IQ_6=str(content.get('IQ_6', '')),
        IQ_7=str(content.get('IQ_7', '')),
        IQ_8=str(content.get('IQ_8', '')),
        IQimage_1=str(content.get('IQimage_1', '')),
        IQimage_2=str(content.get('IQimage_2', '')),
        IQimage_3=str(content.get('IQimage_3', '')),
        IQimage_4=str(content.get('IQimage_4', '')),
        IQimage_5=str(content.get('IQimage_5', '')),
        IQimage_6=str(content.get('IQimage_6', '')),
        IQimage_7=str(content.get('IQimage_7', '')),
        IQimage_8=str(content.get('IQimage_8', '')),
        ASRS=str(content.get('ASRS', '')),
        BIS11=str(content.get('BIS11', '')),
        IUS=str(content.get('IUS', '')),
        LSAS=str(content.get('LSAS', '')),
        SDS=str(content.get('SDS', '')),
        STAI=str(content.get('STAI', '')),
        OCIR=str(content.get('OCIR', '')),
        AQ10=str(content.get('AQ10', '')),
        CFS=str(content.get('CFS', '')),
        MEDIC=str(content.get('MEDIC', ''))
    )

    # BaseObject.check_and_save(questionnairesbehaviour)

    result = {"success": "yes"}

    return jsonify(result)
