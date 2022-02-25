from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 


# Creates Flask instance - app
app=Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

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


@app.route("/candidates", methods=['GET', 'POST'])
def manageCandidates():
    response_obj = {'status': 'success'}
    if request.method == "POST":
        # print(request.is_json)
        post_data = request.json

        person = Candidate.query.filter_by(id=post_data.get('id')).first()

        if person is None:
            person = Candidate(id=post_data.get('id'), name=post_data.get('name'), poiints=post_data.get('points'))
            db.session.add(person)
            db.session.commit()
            response_obj['message'] = "Candidate added!"
        else:
            response_obj['status'] = 'FAILED!'
            response_obj['message'] = "ID already exist! Try again boss man."

    else:

        candidates = Candidate.query.order_by(Candidate.name).all()
        response_obj["Count"] = len(candidates)
        response_obj["candidates"] = []

        for i in range(len(candidates)):
            val = {
                "id" : candidates[i].id,
                "name" : candidates[i].name,
                "points" : candidates[i].poiints

            }
            response_obj["candidates"].append(val)
    return jsonify(response_obj)

@app.route("/add")
def addCandidate():
    return render_template("addCandidate.html")

if __name__ == "__main__":
    app.run(debug=True)
