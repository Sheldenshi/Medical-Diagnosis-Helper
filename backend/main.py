from flask import Flask, request, redirect, url_for, jsonify, json
from web_script import search

app = Flask(__name__, static_folder='../popup/build', static_url_path='/')



@app.route("/", methods = ['GET'])
def index():
    return app.send_static_file('index.html')

def format_result(result):
    formated = {}
    id_num = 0
    for r in result:
        rank = r[0]
        link = r[1]
        relativity = r[2]
        temp = {'id': id_num,
                'rank': rank,
                'link': link,
                'relativity': relativity}
        formated[id_num] = temp
        id_num += 1
    return formated

@app.route('/api/search', methods = ['GET', 'POST'])
def handle_search():
    request_data = json.loads(request.data)
    symptoms = request_data['symptoms']
    diagnoses = request_data['diagnoses']
    result = search(symptoms, diagnoses)
    result = format_result(result)
    return result

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
