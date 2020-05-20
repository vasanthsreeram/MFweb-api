"""users routes"""
from flask import current_app as app, jsonify, request
from models import Task, BaseObject, db
from collections import OrderedDict
import numpy as np
import json
import glob


@app.route('/task/<user_id>/<block_no>', methods=['GET'])

def get_task(user_id,block_no):

    query = Task.query.filter(Task.UserNo==user_id, Task.BlockNo==block_no)
    if query != None:
        print('Exists')
        
    block  = query.all()

    # format the query into a dictionnary first:
        	
    result                          = {}
    
    arr_user                        = [];
    arr_trial                       = [];
    arr_block                       = [];
    arr_horizon                     = [];
    arr_item                        = [];
    arr_unusedTree                  = [];
    arr_initialSampleNb             = [];
    arr_displayOrder                = [];
    arr_TreePositions               = [];
    arr_initialSamplesTree          = [];
    arr_initialSamplesSize          = [];
    arr_Tree1FutureSize             = [];
    arr_Tree2FutureSize             = [];
    arr_Tree3FutureSize             = [];
    arr_Tree4FutureSize             = [];
    
    for t in range(0,100,1):
        
        tmp_user                    = block[t].get_user_no().replace('  ',' ').split(' ')
        tmp_trial                   = block[t].get_trial_no().replace('  ',' ').split(' ')
        tmp_block                   = block[t].get_block_no().replace('  ',' ').split(' ')
        tmp_horizon                 = block[t].get_horizon().replace('  ',' ').split(' ')
        tmp_item                    = block[t].get_item_no().replace('  ',' ').split(' ')
        tmp_unusedTree              = block[t].get_unused_tree().replace('  ',' ').split(' ')
        tmp_initialSampleNb         = block[t].get_initial_sample_nb().replace('  ',' ').split(' ')
        tmp_displayOrder            = block[t].get_display_order()
        tmp_TreePositions           = block[t].get_tree_positions()
        tmp_initialSamplesTree      = block[t].get_initial_samples_tree()
        tmp_initialSamplesSize      = block[t].get_initial_samples_size()
        tmp_Tree1FutureSize         = block[t].get_tree1_future_size()
        tmp_Tree2FutureSize         = block[t].get_tree2_future_size()
        tmp_Tree3FutureSize         = block[t].get_tree3_future_size()
        tmp_Tree4FutureSize         = block[t].get_tree4_future_size()
        
        arr_user.append(int(tmp_user[0])) 
        arr_trial.append(int(tmp_trial[0])) 
        arr_block.append(int(tmp_block[0])) 
        arr_horizon.append(int(tmp_horizon[0])) 
        arr_item.append(int(tmp_item[0]))
        arr_unusedTree.append(int(tmp_unusedTree[0]))
        arr_initialSampleNb.append(int(tmp_initialSampleNb[0]))
        
        arr_initialSamplesTree.append(tmp_initialSamplesTree)
        arr_initialSamplesSize.append(tmp_initialSamplesSize)
        
        arr_TreePositions.append(tmp_TreePositions)
        arr_displayOrder.append(tmp_displayOrder)     
        
        arr_Tree1FutureSize.append(tmp_Tree1FutureSize)
        arr_Tree2FutureSize.append(tmp_Tree2FutureSize)
        arr_Tree3FutureSize.append(tmp_Tree3FutureSize)
        arr_Tree4FutureSize.append(tmp_Tree4FutureSize)
    
    result['UserNo']                 = arr_user     
    result['TrialNo']                = arr_trial
    result['BlockNo']                = arr_block
    result['Horizon']                = arr_horizon
    result['ItemNo']                 = arr_item
    result['UnusedTree']             = arr_unusedTree
    result['TreePositions']          = arr_TreePositions
    result['DisplayOrder']           = arr_displayOrder
    result['InitialSamplesTree']     = arr_initialSamplesTree
    result['InitialSamplesSize']     = arr_initialSamplesSize
    result['InitialSampleNb']        = arr_initialSampleNb
    result['Tree1FutureSize']        = arr_Tree1FutureSize
    result['Tree2FutureSize']        = arr_Tree2FutureSize
    result['Tree3FutureSize']        = arr_Tree3FutureSize
    result['Tree4FutureSize']        = arr_Tree4FutureSize
    

    app.logger.info(result)
    return jsonify(result), 200 