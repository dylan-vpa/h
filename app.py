from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO
import random
import argparse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Store heart positions for real-time updates
hearts = []

@app.route('/')
def index():
    return jsonify({
        'message': '¡Hola Hannah, mi amor! Hice un pequeño detalle para ti 😊💖. Visita /ily, /you, y /heart para ver más.',
        'endpoints': ['/ily', '/you', '/heart']
    })

@app.route('/ily')
def ily():
    return jsonify({
        'message': '💘 TE AMO HANNAH 💘' * 3,
        'emojis': '❤️💕💞'
    })

@app.route('/you')
def you():
    return jsonify({
        'message': 'Tú eres mi persona, Hannah 🌟💖',
        'emojis': '😍💓'
    })

@app.route('/heart')
def heart():
    # ASCII heart, split into lines for animation
    heart_lines = [
        "   **   ",
        " *    * ",
        "*      *",
        " *    * ",
        "   **   "
    ]
    return jsonify({
        'message': 'Un corazón para ti, Hannah, que se forma línea por línea 💖',
        'heart': heart_lines
    })

@app.route('/view')
def view():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    # Initialize some hearts on connect
    for _ in range(5):
        hearts.append({
            'id': random.randint(1, 1000),
            'x': random.randint(0, 100),
            'y': random.randint(0, 100),
            'size': random.randint(20, 50)
        })
    socketio.emit('update_hearts', hearts)

@socketio.on('request_update')
def handle_update():
    # Update heart positions
    for heart in hearts:
        heart['x'] = (heart['x'] + random.randint(-10, 10)) % 100
        heart['y'] = (heart['y'] + random.randint(-10, 10)) % 100
    socketio.emit('update_hearts', hearts)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Flask app on specified port')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the app on')
    args = parser.parse_args()
    socketio.run(app, debug=True, port=args.port)
