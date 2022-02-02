from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] ={
    'HOSTNAME': '165.232.186.203',
    'PORTNAME' :  '27017',
    'DB_NAME': 'elevator',
    'COLLECTION_NAME' : 'elevator details',
}


@app.route("/")
def query_records():
    return render_template("table.html", utc_dt=datetime.datetime.utcnow())

if __name__ == '__main__':
    app.debug = True
    
