from flask import Flask , request , render_template , jsonify , redirect
from flask_pymongo import PyMongo 
from bson import json_util
import json

app = Flask("__name__") 
app.config['MONGODB_SETTINGS'] ={
    'HOSTNAME': '117.247.195.180',
    'PORTNAME' :  '27017',
    'DB_NAME': 'Elevator',
    'COLLECTION_NAME' : 'elevator details',
}


@app.route("/" , methods=['GET','POST'])
def myhome():
    if request.method=='POST':
        a = request.form['elevator_sl.no']
        b = request.form['elevator_deviceid']
        c = request.form["elevators_buttonid"]
        d = request.form["elevator_timestamp"]
        print(a,b,c,d)
    return render_template("list.html")

@app.route("/" , methods=['GET'])
def elevator():
    elevators = db.elevator.find()
    elevators = list(elevators)
    return render_template('list.html')

if __name__ == '__main__':
    app.run(debug=True)
