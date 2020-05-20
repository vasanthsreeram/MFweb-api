"""users routes"""
from flask import current_app as app, jsonify, request
from models import Initialsamples, BaseObject, db
from collections import OrderedDict
import numpy as np
import json
import glob


@app.route('/initial_samples/<user_no>/<item_no>/<sample_no>', methods=['GET'])

def get_initialsamples(user_no,item_no,sample_no):

    query = Initialsamples.query.filter(Initialsamples.UserNo==user_no, Initialsamples.ItemNo==item_no, Initialsamples.SampleNo==sample_no)
    if query != None:
        print('Exists')
        
    block  = query.first_or_404()

    # format the query into a dictionnary first:
	
    result                   = {}
    arr_id                   = block.get_id()
    result['id']             = arr_id
    
    arr_task_item_no         = block.get_item_no()
    result['itemNo']         = arr_task_item_no
    
    arr_unused_tree          = block.get_unused_tree().replace('  ',' ').split(' ')
    result['unusedTree']     = arr_unused_tree[0]
    
    arr_sample_no            = block.get_sample_no()
    result['sampleNo']       = arr_sample_no
    
    arr_user_no              = block.get_user_no().replace('  ',' ').split(' ')
    result['userNo']         = arr_user_no[0]
    
    arr_tree                 = block.get_tree().replace('  ',' ').split(' ')
    result['Tree']           = arr_tree[0]
    
    arr_size                 = block.get_size().replace('  ',' ').split(' ')
    result['Size']           = arr_size[0]
        

    app.logger.info(result)
    return jsonify(result), 200 