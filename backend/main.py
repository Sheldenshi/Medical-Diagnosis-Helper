from flask import Flask, request, redirect, url_for, jsonify, json
from web_script import search

app = Flask(__name__, static_folder='../popup/build', static_url_path='/')



@app.route("/", methods = ['GET'])
def index():
    return app.send_static_file('index.html')

def format_result(result):
    formated = []
    for r in result:
        rank = r[0]
        link = r[1]
        relativity = r[2]
        temp = {'rank': rank,
                'link': link,
                'relativity': relativity}
        formated.append(temp)
    return formated

@app.route('/api/search', methods = ['GET', 'POST'])
def handle_search():
    request_data = json.loads(request.data)
    symptoms = request_data['symptoms']
    diagnoses = request_data['diagnoses']
    result = search(symptoms, diagnoses)
    format_result(result)
    return result



if __name__ == '__main__':
    app.run(debug=True)