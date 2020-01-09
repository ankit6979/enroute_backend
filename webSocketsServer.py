from flask import Flask, render_template
from flask_socketio import SocketIO
import os

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app)
thread =None

@app.route('/')
def sessions():
    print("sessions")
    #return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event', namespace='/ear')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get("PORT_SOCKET", 30000)))
