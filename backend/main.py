from flask import Flask, request, redirect, url_for, jsonify, json
#import web_script
from flask_sqlalchemy import SQLAlchemy
from web_script import search

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///result.db"
db = SQLAlchemy(app)

class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptoms = db.Column(db.Text, nullable=False)
    diagnoses = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f"{self.id} {self.symptoms} {self.diagnoses}"


def input_serializer(input):
    return {
        "id": input.id,
        "symptoms": input.symptoms,
        "diagnoses": input.diagnoses
    }

def create_db():
    db.create_all()

@app.route("/api", methods = ['GET'])
def index():
    create_db()
    result = Result.query.all()
    return jsonify([*map(result_serializer, result)])

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    link = db.Column(db.Text, nullable=False)
    relativity = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f"{self.rank} {self.link} {self.relativity}"

def result_serializer(result):
    return {
        "id":result.id,
        "rank": result.rank,
        "link": result.link,
        "relativity": result.relativity
    }

def add_result_to_database(result):
    for r in result:
        rank = r[0]
        link = r[1]
        relativity = r[2]
        new_result = Result(rank=rank, link=link, relativity=relativity)
        db.session.add(new_result)
        db.session.commit()
@app.route('/api/input', methods = ['GET', 'POST'])
def handle_input():
    request_data = json.loads(request.data)
    symptoms = request_data['symptoms']
    diagnoses = request_data['diagnoses']
    create_db()
    result = search(symptoms, diagnoses)
    add_result_to_database(result)
    return {'201': 'input added successfully'}



if __name__ == '__main__':
    app.run(debug=True)