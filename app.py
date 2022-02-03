from flask import Flask, render_template,request,redirect,url_for 
from bson import ObjectId 
from pymongo import MongoClient
import os

app = Flask(__name__)
title = "Elevator Details"
heading = "Elevator Details"

client = MongoClient("mongodb://127.0.0.1:27017") 
db = client.elevator    
elevator = db.elevatordetails 


@app.route("/", methods=['POST'])
def action ():
	Sl.no=request.values.get("Sl.no")
	Deviceid=request.values.get("Device id")
	Buttonid=request.values.get("Button id")
	Timestamp=request.values.get("Timestamp")
	return redirect("/")


@app.route("/", methods=['GET'])
def search():
	key=request.values.get("key")
	refer=request.values.get("refer")
	if(key=="_id"):
		elevator_l = elevator.find({refer:ObjectId(key)})
	else:
		elevator_l = elevator.find({refer:key})
	return render_template('home.html',elevator=elevator_l,t=title,h=heading)

if __name__ == "__main__":

    app.run()
