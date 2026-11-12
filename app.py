import os

import flask
from flask_wtf.csrf import CSRFProtect

import validation
from data import ISEN_LOCATION, REPORTS, add_report, find_report

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

csrf = CSRFProtect(app)


@app.route("/")
def home():
    return flask.render_template("index.html")


@app.route("/reports")
def reports():
    return flask.render_template("list.html", reports=REPORTS)


@app.route("/reports/<int:id>")
def report(id):
    element = find_report(id)
    if element is None:
        flask.abort(404)
    return flask.render_template("detail.html", report=element)


@app.route("/reports/new", methods=["GET", "POST"])
def new_report():
    values = {"title": "", "description": ""}
    errors = {}

    if flask.request.method == "POST":
        values["title"] = flask.request.form.get("title", "").strip()
        values["description"] = flask.request.form.get("description", "").strip()
        errors = validation.validate_report(values["title"], values["description"])

        if not errors:
            created = add_report(values["title"], values["description"])
            flask.flash("Report created successfully.")
            return flask.redirect(flask.url_for("report", id=created["id"]), code=303)

    return flask.render_template(
        "new.html",
        values=values,
        errors=errors,
        limits=validation,
    ), 400 if errors else 200


@app.route("/map")
def map():
    return flask.render_template("map.html", location=ISEN_LOCATION)


@app.errorhandler(404)
def not_found(error):
    return flask.render_template("404.html"), 404
