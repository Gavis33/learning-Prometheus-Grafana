import time 
import random
from flask import Flask, jsonify

app = Flask(__name__)

# Simulated metrics
total_requests = 0

@app.route('/metrics', methods=['GET'])
def metrics():
    global total_requests
    total_requests += 1

    # Simulated values
    # round(random.uniform(initial_value, final_value), decimal_places)
    request_processing_latency = round(random.uniform(0.1, 1.5), 3)
    model_prediction_success_rate = round(random.uniform(80, 100), 2)

    # Return metrics in Prometheus format
    prometheus_metrics = (
        "# HELP total_requests\n"
        "# TYPE total_requests counter\n"
        f"total_requests {total_requests}\n"
        "# HELP request_processing_latency_seconds\n"
        "# TYPE request_processing_latency_seconds gauge\n"
        f"request_processing_latency_seconds {request_processing_latency}\n"
        "# HELP model_prediction_success_rate\n"
        "# TYPE model_prediction_success_rate gauge\n"
        f"model_prediction_success_rate {model_prediction_success_rate}\n"
    )

    # Return the metrics in plain text format where 200 is the HTTP status code, and the content type is set to plain text, charset utf-8 is used for encoding the text data
    return prometheus_metrics, 200, {"Content-Type": "text/plain; charset=utf-8"}

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to Flask Metrics app... Go to http://localhost:5000/metrics"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)