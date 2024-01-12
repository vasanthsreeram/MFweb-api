"""users routes"""
from flask import current_app as app, jsonify
from models import Training
from sqlalchemy.orm import selectinload  # New import for eager loading

@app.route('/training/<user_id>', methods=['GET'])
def get_training(user_id):
    # Updated query to fetch a single record
    query = Training.query.filter(Training.UserNo == user_id).first()

    if query:
        result = {
            'UserNo': int(query.get_user_no().replace('  ', ' ').split(' ')[0]),
            'TrialNo': int(query.get_trial_no().replace('  ', ' ').split(' ')[0]),
            'InitialSamplesSize': query.get_initial_samples_size(),
            'ChoicesSize': query.get_choices_size(),
            'ChoicesCorrect': query.get_choices_correct()
        }
        app.logger.info(result)
        return jsonify(result), 200
    else:
        # Handle the case when the record doesn't exist
        return jsonify({'error': 'Record not found'}), 404
