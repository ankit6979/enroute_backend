import json
from mongodb_functions import *
from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route("/api/ads", methods = ['POST', 'GET'])
# def getData():
#     if request.method == 'POST':
#         req_json = request.get_json();
#         path = req_json['ad_path']
#         zipCode = req_json['zipcode']
#         adCategory = req_json['ad_type']
#         textContent = req_json['text_content']
#         location = req_json['location']

#         SaveInDB.saveData(path, zipCode, adCategory, textContent, location)
#         return "It works!"

#     if request.method == 'GET':
#         group_name = request.args.get('dataBy')
#         print(group_name)
#         return json.dumps(SaveInDB.fetchData(group_name))


@app.route("/api/uploadFile", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # response = app.response_class(
        #     response=json.dumps("downloads//uploaded//" + filename),
        #     status=200,
        #     mimetype='application/json'
        # )
        # return response
        return '200'


@app.route("/api/uploadData", methods=['POST', 'GET'])
def save():
    if request.method == 'POST':
        req_json = request.get_json()
        language = req_json['language']
        genre = req_json['genre']
        name = req_json['name']
        url = req_json['url']

        saveData(language, genre, name, url)

        response = app.response_class(
            response=json.dumps(req_json),
            status=200,
            mimetype='application/json'
        )
        return response


@app.route('/upload', methods=['POST'])
def file_upload():
    # print(request.files)
    # checking if the file is present or not.
    # if 'file' not in request.files:
    #     return "No file found"
    file = request.files['file']
    file.save("static/test.jpg")
    return "file successfully saved"


@app.route("/api/queryData", methods=['POST', 'GET'])
def getData():
    if request.method == 'POST':
        req_json = request.get_json()
        language = req_json['language']
        genre = req_json['genre']
        resp = queryData(language, genre)

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/api/deleteData", methods=['POST', 'GET'])
def deleteData():
    if request.method == 'POST':
        req_json = request.get_json()
        language = req_json['language']
        genre = req_json['genre']
        name = req_json['name']
        resp = deleteData(language, genre, name)

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
