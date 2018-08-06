from flask import Flask, render_template
from torre import get_bio

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/torrebio/<string:personid>", methods=["GET"])
def get_torrebio_html(personid):
    torrebio = get_bio(personid)
    print(torrebio)
    return render_template("torrebio.html", bio=torrebio)
