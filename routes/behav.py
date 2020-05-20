"""users routes"""
from flask import current_app as app, jsonify
from models import Training

@app.route('/training/<user_id>', methods=['GET'])

def get_training(user_id):

    query = Training.query.filter(Training.UserNo==user_id)
    if query != None:
        print('Exists')
        
    block  = query.all()

    # format the query into a dictionnary first:
        	
    result                          = {}
    
    arr_user                        = [];
    arr_trial                       = [];
    arr_initialSamplesSize          = [];
    arr_choicesSize                 = [];
    arr_choicesCorrect              = [];
    
    for t in range(0,10,1):
        
        tmp_user                    = block[t].get_user_no().replace('  ',' ').split(' ')
        tmp_trial                   = block[t].get_trial_no().replace('  ',' ').split(' ')
        tmp_initialSamplesSize      = block[t].get_initial_samples_size()
        tmp_choicesSize             = block[t].get_choices_size()
        tmp_choicesCorrect          = block[t].get_choices_correct()
        
        arr_user.append(int(tmp_user[0])) 
        arr_trial.append(int(tmp_trial[0])) 
        arr_initialSamplesSize.append(tmp_initialSamplesSize)
        arr_choicesSize.append(tmp_choicesSize)
        arr_choicesCorrect.append(tmp_choicesCorrect)     

    result['UserNo']                 = arr_user     
    result['TrialNo']                = arr_trial
    result['InitialSamplesSize']     = arr_initialSamplesSize
    result['ChoicesSize']            = arr_choicesSize
    result['ChoicesCorrect']         = arr_choicesCorrect

    app.logger.info(result)
    return jsonify(result), 200 