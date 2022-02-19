from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Creates Flask instance - app
app = Flask(__name__)

# add database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///candidates.db'
db = SQLAlchemy(app)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    poiints = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Candidate %r>' %self.name 


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/candidates")
def displayCandidateTable():
    candidates = Candidate.query.order_by(Candidate.name).all()
    ret = {
        "Count" : len(candidates),
        "candidates" : []
    }

    for i in range(len(candidates)):
        val = {
            "id" : candidates[i].id,
            "name" : candidates[i].name,
            "points" : candidates[i].poiints

        }
        ret["candidates"].append(val)
    return ret

if __name__ == "__main__":
    app.run(debug=True)

