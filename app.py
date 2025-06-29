from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mythos_secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('attack')
def on_attack(data):
    print("Attack received:", data)
    emit('update_health', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
