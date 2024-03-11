"""users routes"""
from flask import current_app as app, jsonify, request
from models import Behaviour, BaseObject

@app.route('/behaviour/<user_id>/<blockNo>', methods=['POST', 'GET'])
def create_behaviour(user_id, blockNo):
    content = request.json
    print(content)
    print(f'user id:{user_id}, block no: {blockNo}')
    behaviour = Behaviour()

    behaviour.UserNo=int(user_id)
    behaviour.Date=str(content.get('Date', ''))
    behaviour.UserStartTime=str(content.get('UserStartTime', ''))
    behaviour.ProlificID=str(content.get('ProlificID', ''))
    behaviour.TrainingNo=str(content.get('TrainingNo', ''))
    behaviour.TaskNo=str(content.get('TaskNo', ''))
    behaviour.BlockNo=int(blockNo)
    behaviour.InfoRequestNo=str(content.get('InfoRequestNo', ''))
    behaviour.BlockStartTime=str(content.get('BlockStartTime', ''))
    behaviour.BlockFinishTime=str(content.get('BlockFinishTime', ''))
    behaviour.TreeColours=str(content.get('TreeColours', ''))
    behaviour.ChosenTree=str(content.get('ChosenTree', ''))
    behaviour.ChosenAppleSize=str(content.get('ChosenAppleSize', ''))
    behaviour.AllKeyPressed=str(content.get('AllKeyPressed', ''))
    behaviour.ReactionTimes=str(content.get('ReactionTimes', ''))
    behaviour.Horizon=str(content.get('Horizon', ''))
    behaviour.ItemNo=str(content.get('ItemNo', ''))
    behaviour.TrialNo=str(content.get('TrialNo', ''))
    behaviour.UnusedTree=str(content.get('UnusedTree', ''))
    behaviour.InitialSamplesNb=str(content.get('InitialSamplesNb', ''))
    behaviour.InitialSamplesTree=str(content.get('InitialSamplesTree', ''))
    behaviour.InitialSamplesSize=str(content.get('InitialSamplesSize', ''))
    behaviour.TreePositions=str(content.get('TreePositions', ''))
    
    print(behaviour.get_user_date())
    print(behaviour.get_user_start_time())
    print(behaviour.get_task_player_id())
    print(behaviour.get_user_no())
    print(str(content.get('Date', '')))
    print(content.get('TaskNo', ''))
    BaseObject.check_and_save(behaviour)

    result = {"success": "yes"}

    return jsonify(result)
