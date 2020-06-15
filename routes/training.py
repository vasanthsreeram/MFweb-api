"""users routes"""
from flask import current_app as app, jsonify
from models import Training

@app.route('/training/<training_no>', methods=['GET'])

def get_training(training_no):

    query = Training.query.filter(Training.TrainingNo==training_no)
    if query != None:
        print('Exists')
        
    block  = query.all()

    # format the query into a dictionnary first:
        	
    result                          = {}
    
    arr_trainingno                        = [];
    arr_trial                       = [];
    arr_initialSamplesSize          = [];
    arr_choicesSize                 = [];
    arr_choicesCorrect              = [];
    
    for t in range(0,10,1):
        
        tmp_trainingno              = block[t].get_training_no().replace('  ',' ').split(' ')
        tmp_trial                   = block[t].get_trial_no().replace('  ',' ').split(' ')
        tmp_initialSamplesSize      = block[t].get_initial_samples_size()
        tmp_choicesSize             = block[t].get_choices_size()
        tmp_choicesCorrect          = block[t].get_choices_correct()
        
        arr_trainingno.append(int(tmp_trainingno[0])) 
        arr_trial.append(int(tmp_trial[0])) 
        arr_initialSamplesSize.append(tmp_initialSamplesSize)
        arr_choicesSize.append(tmp_choicesSize)
        arr_choicesCorrect.append(tmp_choicesCorrect)     

    result['TrainingNo']             = arr_trainingno     
    result['TrialNo']                = arr_trial
    result['InitialSamplesSize']     = arr_initialSamplesSize
    result['ChoicesSize']            = arr_choicesSize
    result['ChoicesCorrect']         = arr_choicesCorrect

    app.logger.info(result)
    return jsonify(result), 200 