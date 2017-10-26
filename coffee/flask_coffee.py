"""
DOCUMENTATION HERE
"""

from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    print("Opening for global access on port {}".format(8000))
    app.run(port=8000, host="0.0.0.0")
