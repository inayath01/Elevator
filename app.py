from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def table():
    return render_template("table.html", utc_dt=datetime.datetime.utcnow())
