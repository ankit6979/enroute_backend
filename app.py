# app.py
from flask import Flask, request, jsonify
import json
# from mongodb_functions import *

app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    name = request.form.get('name')
    print(name)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if name:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

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

@app.route("/languages", defaults={'language': None}, methods=['GET'])
def get_language(language):
    if request.method == 'GET':
        language = request.args.get('language')
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