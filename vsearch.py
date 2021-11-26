from flask import Flask, jsonify , request , render_template 
from flask_sqlalchemy import SQLAlchemy
from app import app
import time
from datetime import datetime, timedelta
from datetime import date


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///vsearch.db"
db = SQLAlchemy(app)


class log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_date = db.Column(db.DateTime, nullable=False,default = datetime.now())
    phrase = db.Column(db.String(121) , nullable = False)
    letter = db.Column(db.String(40) , nullable = False)
    ip = db.Column(db.String(15) , nullable = False)
    browser_string = db.Column(db.String(260) , nullable = False)
    result = db.Column(db.String(20) , nullable = False)

db.create_all()