from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
# This line is the only thing needed to expose metrics
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return "Hello, Metrics!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)