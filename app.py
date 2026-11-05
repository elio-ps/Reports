
import flask

app = flask.Flask(__name__)

REPORTS_TYPE = [
    {"id": 1, "name": "Inappropriate content"},
    {"id": 2, "name": "Harassment"},
    {"id": 3, "name": "Spam"},
    {"id": 4, "name": "Scam / Fraud"},
    {"id": 5, "name": "Identity theft"},
    {"id": 6, "name": "Hate speech"},
    {"id": 7, "name": "Violence / Threats"},
    {"id": 8, "name": "Illegal content"},
    {"id": 9, "name": "Misinformation"},
    {"id": 10, "name": "Technical issue"},
    {"id": 11, "name": "Copyright infringement"},
    {"id": 12, "name": "Other"}
]

@app.route("/")
def home():
    return flask.render_template("index.html", reports=REPORTS_TYPE)

@app.route("/report/<int:id>")
def report(id):
    for element in REPORTS_TYPE:
        if element["id"] == id:
            return flask.render_template(
                "detail.html", element=element
            )

    flask.abort(404)
