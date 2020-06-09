"""users routes"""
from flask import current_app as app, jsonify, request
from models import Behaviour, BaseObject


@app.route('/behaviour/<user_id>/<blockNo>', methods=['POST', 'GET'])

def create_behaviour(user_id, blockNo):
    
    content     = request.json        
    behaviour   = Behaviour()

    behaviour.UserNo                = int(user_id)
    behaviour.UserStartTime = str(content['UserStartTime'])
    behaviour.BlockNo               = int(blockNo)
    behaviour.BlockStartTime        = str(content['BlockStartTime'])
    behaviour.BlockFinishTime       = str(content['BlockFinishTime'])
    behaviour.TreeColours           = str(content['TreeColours'])
    behaviour.ChosenTree            = str(content['ChosenTree'])
    behaviour.ChosenAppleSize       = str(content['ChosenAppleSize'])
    behaviour.AllKeyPressed         = str(content['AllKeyPressed'])
    behaviour.ReactionTimes         = str(content['ReactionTimes'])
    behaviour.Horizon               = str(content['Horizon'])
    behaviour.ItemNo                = str(content['ItemNo'])
    behaviour.TrialNo               = str(content['TrialNo'])
    behaviour.UnusedTree            = str(content['UnusedTree'])
    behaviour.InitialSamplesNb      = str(content['InitialSamplesNb'])
    behaviour.InitialSamplesTree    = str(content['InitialSamplesTree'])
    behaviour.InitialSamplesSize    = str(content['InitialSamplesSize'])
    behaviour.TreePositions         = str(content['TreePositions'])
     
    BaseObject.check_and_save(behaviour)

    result = dict({"success": "yes"}) 
    
    return jsonify(result)