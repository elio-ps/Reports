import flask

from data import ISEN_LOCATION, REPORTS

app = flask.Flask(__name__)


@app.route("/")
def home():
    return flask.render_template("index.html")


@app.route("/reports")
def reports():
    return flask.render_template("list.html", reports=REPORTS)


@app.route("/report/<int:id>")
def report(id):
    for element in REPORTS:
        if element["id"] == id:
            return flask.render_template("detail.html", report=element)

    flask.abort(404)


@app.route("/map")
def map():
    return flask.render_template("map.html", location=ISEN_LOCATION)


@app.errorhandler(404)
def not_found(error):
    return flask.render_template("404.html"), 404
