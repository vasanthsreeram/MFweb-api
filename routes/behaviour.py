"""users routes"""
from flask import current_app as app, jsonify, request
from models import Behaviour, BaseObject

@app.route('/behaviour/<user_id>/<blockNo>', methods=['POST', 'GET'])
def create_behaviour(user_id, blockNo):
    content = request.json

    behaviour = Behaviour(
        UserNo=int(user_id),
        Date=str(content.get('Date', '')),
        UserStartTime=str(content.get('UserStartTime', '')),
        ProlificID=str(content.get('ProlificID', '')),
        TrainingNo=str(content.get('TrainingNo', '')),
        TaskNo=str(content.get('TaskNo', '')),
        BlockNo=int(blockNo),
        InfoRequestNo=str(content.get('InfoRequestNo', '')),
        BlockStartTime=str(content.get('BlockStartTime', '')),
        BlockFinishTime=str(content.get('BlockFinishTime', '')),
        TreeColours=str(content.get('TreeColours', '')),
        ChosenTree=str(content.get('ChosenTree', '')),
        ChosenAppleSize=str(content.get('ChosenAppleSize', '')),
        AllKeyPressed=str(content.get('AllKeyPressed', '')),
        ReactionTimes=str(content.get('ReactionTimes', '')),
        Horizon=str(content.get('Horizon', '')),
        ItemNo=str(content.get('ItemNo', '')),
        TrialNo=str(content.get('TrialNo', '')),
        UnusedTree=str(content.get('UnusedTree', '')),
        InitialSamplesNb=str(content.get('InitialSamplesNb', '')),
        InitialSamplesTree=str(content.get('InitialSamplesTree', '')),
        InitialSamplesSize=str(content.get('InitialSamplesSize', '')),
        TreePositions=str(content.get('TreePositions', ''))
    )

    BaseObject.check_and_save(behaviour)

    result = {"success": "yes"}

    return jsonify(result)
