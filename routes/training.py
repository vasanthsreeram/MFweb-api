"""users routes"""
from flask import current_app as app, jsonify
from models import Training


@app.route('/training/<training_no>', methods=['GET'])
def get_training(training_no):
    query = Training.query.filter(Training.TrainingNo == training_no).first()

    if query:
        print('Exists', query)
        
        result = {
            'TrainingNo': int(query.get_training_no().replace('  ', ' ').split(' ')[0]),
            'TrialNo': int(query.get_trial_no().replace('  ', ' ').split(' ')[0]),
            'InitialSamplesSize': query.get_initial_samples_size(),
            'ChoicesSize': query.get_choices_size(),
            'ChoicesCorrect': query.get_choices_correct()
        }

        app.logger.info(result)
        print(result)
        return jsonify(result), 200
    else:
        print("no data found")
        return 404
