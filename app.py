# app.py
from flask import Flask, request, jsonify
import json
# from mongodb_functions import *

app = Flask(__name__)

@app.route("/genres", defaults={'genre': None}, methods=['GET'])
def get_genre(genre):
    if request.method == 'GET':
        genre = request.args.get('genre')
        if genre == None:
            resp = ['Action', 'Horror']
        else:
            resp = [{"genre":"Horror","all":50,"few":[{"name":"Star Wars","url":"http://stream.starwars","posterUrl":"http://pic","views":23,"likes":13,"language":"english","comments":[{"userName":"Rey","comment":"Star Blood"}]}]},{"genre":"Action","all":50,"few":[{"name":"Jumanji","url":"http://stream.jumanji","posterUrl":"http://pic","views":67,"likes":55,"language":"english","comments":[{"userName":"Switch","comment":"punchy"}]}]}]

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/languages", defaults={'languages': None}, methods=['GET'])
def get_language():
    if request.method == 'GET':
        language = request.args.get('languages')
        if language == None:
            resp = ['English', 'Hindi']
        else:
            resp = [{"genre":"Horror","all":50,"few":[{"name":"Star Wars","url":"http://stream.starwars","posterUrl":"http://pic","views":23,"likes":13,"language":"english","comments":[{"userName":"Rey","comment":"  Star Blood"}]}]},{"genre":"Action","all":50,"few":[{"name":"Jumanji","url":"http://stream.jumanji","posterUrl":"http://pic","views":67,"likes":55,"language":"english","comments":[{"userName":"Switch","comment":"punchy"}]}]}]

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(host='0.0.0.0', threaded=True, port=5000)