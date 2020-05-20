"""users routes"""
from flask import current_app as app, jsonify, request
from models import Trial, BaseObject, db
from collections import OrderedDict
import numpy as np
import json
import glob


@app.route('/trial/<user_id>/<trial_no>', methods=['GET'])

def get_trial(user_id,trial_no):

    query = Trial.query.filter(Trial.UserNo==user_id, Trial.TrialNo==trial_no)
    if query != None:
        print('Exists')
        
    block  = query.first_or_404()

    # format the query into a dictionnary first:
	
    result                   = {}
    arr_id                   = block.get_id().replace('  ',' ').split(' ')
    result['id']             = arr_id[0]
    
    arr_task_id              = block.get_task_id().replace('  ',' ').split(' ')
    result['taskID']         = arr_task_id[0]
    
    arr_user_no              = block.get_user_no().replace('  ',' ').split(' ')
    result['userNo']         = arr_user_no[0]
    
    arr_item_no              = block.get_item_no().replace('  ',' ').split(' ')
    result['itemNo']         = arr_item_no[0]
    
    arr_horizon               = block.get_horizon().replace('  ',' ').split(' ')
    result['horizon']         = arr_horizon[0]
    
    arr_block_no              = block.get_block_no().replace('  ',' ').split(' ')
    result['blockNo']         = arr_block_no[0]
        
    arr_trial_no              = block.get_trial_no().replace('  ',' ').split(' ')
    result['trialNo']         = arr_trial_no[0]
    
    arr_sample_nb             = block.get_sample_nb().replace('  ',' ').split(' ')
    result['sampleNb']        = arr_sample_nb[0]


    app.logger.info(result)
    return jsonify(result), 200 