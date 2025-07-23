from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from a secure, non-root Python container!"

if __name__ == '__main__':
    # The app will run on port 5000 inside the container
    app.run(host='0.0.0.0', port=5000)