"""users routes"""
from flask import current_app as app, jsonify, request
from models import Task
from sqlalchemy.orm.exc import NoResultFound

@app.route('/task/<task_no>/<block_no>', methods=['GET'])
def get_task(task_no, block_no):
    try:
        query = Task.query.filter(Task.TaskNo == task_no, Task.BlockNo == block_no).all()
        
        if query:
            print('Exists')
            result = {
                'TaskNo': [],
                'TrialNo': [],
                'BlockNo': [],
                'Horizon': [],
                'ItemNo': [],
                'UnusedTree': [],
                'InitialSampleNb': [],
                'DisplayOrder': [],
                'TreePositions': [],
                'InitialSamplesTree': [],
                'InitialSamplesSize': [],
                'Tree1FutureSize': [],
                'Tree2FutureSize': [],
                'Tree3FutureSize': [],
                'Tree4FutureSize': []
            }
            
            for item in query:
                result['TaskNo'].append(int(item.get_task_no()))
                result['TrialNo'].append(int(item.get_trial_no()))
                result['BlockNo'].append(int(item.get_block_no()))
                result['Horizon'].append(int(item.get_horizon()))
                result['ItemNo'].append(int(item.get_item_no()))
                result['UnusedTree'].append(int(item.get_unused_tree()))
                result['InitialSampleNb'].append(int(item.get_initial_sample_nb()))
                result['DisplayOrder'].append(item.get_display_order())
                result['TreePositions'].append(item.get_tree_positions())
                result['InitialSamplesTree'].append(item.get_initial_samples_tree())
                result['InitialSamplesSize'].append(item.get_initial_samples_size())
                result['Tree1FutureSize'].append(item.get_tree1_future_size())
                result['Tree2FutureSize'].append(item.get_tree2_future_size())
                result['Tree3FutureSize'].append(item.get_tree3_future_size())
                result['Tree4FutureSize'].append(item.get_tree4_future_size())
            
            app.logger.info(result)
            return jsonify(result), 200
        else:
            return jsonify({'error': 'No records found'}), 404

    except NoResultFound:
        return jsonify({'error': 'No records found'}), 404
