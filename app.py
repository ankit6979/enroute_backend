# app.py
from flask import Flask, request
import json
import mongodb_functions
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route("/map", methods=['POST'])
def getMap():
    if request.method == 'POST':
        req_json = request.get_json()
        pnr = req_json['pnr']
        response = app.response_class(
            response=json.dumps(mongodb_functions.getCoordinates(pnr)),
            status=200,
            mimetype='application/json'
        )
    return response


@app.route("/home", methods=['POST'])
def home():
    if request.method == 'POST':
        req_json = request.get_json()
        pnr = req_json['pnr']
        response = app.response_class(
            response=json.dumps(mongodb_functions.getContent(pnr)),
            status=200,
            mimetype='application/json'
        )
    return response


@app.route("/content", methods=['POST', 'GET'])
def updateContent():
    if request.method == 'POST':
        req_json = request.get_json()
        pnr = req_json['pnr']
        media_id = req_json['mediaid']
        viewflag = req_json['viewflag']
        likeflag = req_json['likeflag']
        comments = req_json['comments']
        anonymousflag = req_json['aflag']

        response = app.response_class(
            response=json.dumps(mongodb_functions.AddContent(
                pnr, media_id, viewflag, likeflag, comments, anonymousflag)),
            status=200,
            mimetype='application/json'
        )
    if request.method == 'GET':
        media_id = request.args.get('mediaid')
        resp = mongodb_functions.getMediaDetails(media_id)
        response = app.response_class(
            response=json.dumps(resp),
            status=200,
            mimetype='application/json'
        )
    return response


@app.route("/preferenceSelect", methods=['POST'])
def updatePreference():
    if request.method == 'POST':
        req_json = request.get_json()
        pnr = req_json['pnr']
        name = req_json['name']
        lang_pref = req_json['lang_pref']
        genre_pref = req_json['genre_pref']

        response = app.response_class(
            response=json.dumps(mongodb_functions.userPreference(
                pnr, name, lang_pref, genre_pref)),
            status=200,
            mimetype='application/json'
        )
    return response


@app.route("/login", methods=['POST'])
def check():
    if request.method == 'POST':
        req_json = request.get_json()
        pnr = req_json['pnr']
        name = req_json['name']
        seatno = req_json['seatno']

        response = app.response_class(
            response=json.dumps(
                mongodb_functions.checkUser(pnr, name, seatno)),
            status=200,
            mimetype='application/json'
        )
    return response


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
        description = req_json['description']
        thumbnailurl = req_json['thumbnail']
        mongodb_functions.saveData(
            language, genre, name, url, description, thumbnailurl)

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
        resp = mongodb_functions.queryData(language, genre)

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/api/deleteData", methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        req_json = request.get_json()
        language = req_json['language']
        genre = req_json['genre']
        name = req_json['name']
        resp = mongodb_functions.deleteData(language, genre, name)

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/genres", methods=['GET'])
def get_genre():
    if request.method == 'GET':
        genre = request.args.get('genre')
        resp = mongodb_functions.queryGenre(genre)
        #resp = [{"genre":"Horror","all":50,"few":[{"name":"Star Wars","url":"http://stream.starwars","posterUrl":"http://pic","views":23,"likes":13,"language":"english","comments":[{"userName":"Rey","comment":"Star Blood"}]}]},{"genre":"Action","all":50,"few":[{"name":"Jumanji","url":"http://stream.jumanji","posterUrl":"http://pic","views":67,"likes":55,"language":"english","comments":[{"userName":"Switch","comment":"punchy"}]}]}]

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/languages", methods=['GET'])
def get_language():
    if request.method == 'GET':
        language = request.args.get('language')
        resp = mongodb_functions.queryLanguage(language)
        #resp = [{"genre":"Horror","all":50,"few":[{"name":"Star Wars","url":"http://stream.starwars","posterUrl":"http://pic","views":23,"likes":13,"language":"english","comments":[{"userName":"Rey","comment":"  Star Blood"}]}]},{"genre":"Action","all":50,"few":[{"name":"Jumanji","url":"http://stream.jumanji","posterUrl":"http://pic","views":67,"likes":55,"language":"english","comments":[{"userName":"Switch","comment":"punchy"}]}]}]

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(host='0.0.0.0', threaded=True, port=int(os.environ['PORT_APP']))
