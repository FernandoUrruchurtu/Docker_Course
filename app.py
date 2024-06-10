import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Fernando Urruchurtu",
        "socialMedia":
        [
            {"facebookUser":"fernandourruchurtu"},
            {"instagramUser":"furruchurtu"}
        ],
        "author":"Fernando Urruchurtu"
    }
    return json.dumps(value)