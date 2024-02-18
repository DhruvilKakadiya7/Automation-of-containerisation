from flask import Flask, jsonify, request, Response, stream_with_context, json
import docker
import subprocess
import os
import re
import random
from util import get_container_stats
from flask_cors import CORS, cross_origin
import threading
import time

app = Flask(__name__)
cors = CORS(app)

def stream_json_data():
    client = docker.from_env()
    container = client.containers.get("499731b3472a44680fbcfe965956fa789a5884232ebdc804462d9e443fa0130a")
    for stats in container.stats(stream=True):
        # Process stats according to your requirements
        # processed_stats = process_stats(stats)  # Implement your processing logic here
        stats = stats.decode("utf-8") 
        print(stats)
        yield json.dumps(stats)  # Yield JSON-formatted data
        time.sleep(1)  # Simulate 1-second update interval

@app.route('/api/stream', methods=['GET'])
def visualize():
    def generate():
        for data in stream_json_data():
            yield data

    response = Response(generate(), mimetype='application/json')
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Connection'] = 'keep-alive'
    return response

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
