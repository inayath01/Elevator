from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] ={
    'db': 'elevator',
    'host': 'localhost',
    'port' :  '27017',
}


@app.route("/")
def query_records():
    return render_template("table.html")

if __name__ == '__main__':
    app.debug = True
    
