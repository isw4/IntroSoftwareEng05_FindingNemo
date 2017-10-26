"""
DOCUMENTATION HERE
"""

from flask import Flask, url_for, render_template
import config
import logging

###
# Globals
###
app = Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY


@app.route("/")
def index():
    return render_template('index.html')

#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")