"""
DOCUMENTATION HERE
"""

import flask
from flask import Flask, url_for, render_template
import config
import logging
import pre

###
# Globals
###
app = Flask(__name__)

app.logger.debug("Getting the configuration")
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

app.logger.debug("Getting the list of sushi restaurants")
rest_data = pre.process(open(CONFIG.POI_FILE))

@app.route("/")
def index():
    flask.g.data = rest_data
    app.logger.debug("Rendering the main page")
    return render_template('index.html')

#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
