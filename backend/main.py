import time
import flask

app = flask.Flask(__name__)

@app.route("/time")
def get_current_time():
    return {'time': time.time()}

