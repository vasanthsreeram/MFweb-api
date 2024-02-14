'''
	Script qui lance le backend (database)
'''
import os
import warnings
import urllib
# Flask: interagit avec la base de donnees
from flask_cors import CORS
from flask import Flask, jsonify, request, render_template
from flask_mail import Mail, Message

from models.db import db
from models.install import install_models
from dotenv import load_dotenv
from config import config
load_dotenv()
warnings.filterwarnings("ignore")

# mail = Mail()
app  = Flask(__name__)

# -------------------------
# --- DB configuration ----
# # -------------------------
# username = os.environ.get("username")
# password = os.environ.get("password")
# server = os.environ.get("server")
# database = os.environ.get("database")

username = "gridgame"
password = "J35pZyjo9kLQjh"
server = "clic.database.windows.net"
database = "clic"


db_uri = f"mssql+pymssql://{username}:{password}@{server}/{database}"
print(db_uri)

# Configure Flask app with database URI
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    port = int(os.environ.get("PORT", 4545))
    app.run(host="0.0.0.0", port=port,debug=False)
