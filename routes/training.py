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
        return jsonify(result), 200
    else:
        print("sending fake data")
        result = {
                    "TrainingNo": 1,
                    "TrialNo": 4,
                    "InitialSamplesSize": [
                        [5, 10, 15],   # Data for trial 1
                        [6, 11, 16],   # Data for trial 2
                        [7, 12, 17],   # Data for trial 3
                        [8, 13, 18]    # Data for trial 4
                    ],
                    "ChoicesSize": [
                        [2, 5, 7],     # Data for trial 1
                        [3, 6, 8],     # Data for trial 2
                        [4, 7, 9],     # Data for trial 3
                        [5, 8, 10]     # Data for trial 4
                    ],
                    "ChoicesCorrect": [
                        [1, 0, 1],     # Data for trial 1
                        [0, 1, 0],     # Data for trial 2
                        [1, 1, 1],     # Data for trial 3
                        [0, 0, 1]      # Data for trial 4
                    ]
                }


        return jsonify(result), 200
