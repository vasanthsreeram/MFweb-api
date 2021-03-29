'''
	Script qui lance le backend (database)
'''
import os
import warnings

# Flask: interagit avec la base de donnees
from flask_cors import CORS
from flask import Flask, jsonify, request, render_template
from flask_mail import Mail, Message

from models.db import db
from models.install import install_models

from config import config

warnings.filterwarnings("ignore")

# mail = Mail()
app  = Flask(__name__)

# -------------------------
# --- DB configuration ----
# -------------------------

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('Database Parameters','database_url')

db.init_app(app)
CORS(app)

with app.app_context():
    install_models()
    import routes


# --- TESTING THE SERVER IS WORKING -----------
@app.route('/testmethod', methods=['GET', 'POST'])
def mytest():
    result = dict()
    result['test'] = 'ok'
    return jsonify(result), 200


###########################################################
# let's start
###########################################################

if __name__ == '__main__':
    print("Starting webserver.")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port,debug=False)
