from flask import Flask, request, redirect, url_for, jsonify, json
#import web_script
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
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


@app.route("/api", methods = ['GET'])
def index():
    input = Input.query.all()
    return jsonify([*map(input_serializer, input)])

@app.route('/api/input', methods = ['POST'])
def handle_input():
    request_data = json.loads(request.data)
    symptoms = request_data['symptoms']
    diagnoses = request_data['diagnoses']
    """
    input = Input(symptoms=request_data['symptoms'], diagnoses=request_data['diagnoses'])
    db.session.add(input)
    db.session.commit()
    """
    return {'201': 'input added successfully'}

if __name__ == '__main__':
    app.run(debug=True)