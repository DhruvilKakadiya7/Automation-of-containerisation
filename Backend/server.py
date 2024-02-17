from flask import Flask, jsonify, request
import docker
import subprocess
import os
import re
import random

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "Item 1", "description": "Description of Item 1"},
    {"id": 2, "name": "Item 2", "description": "Description of Item 2"},
    {"id": 3, "name": "Item 3", "description": "Description of Item 3"}
]

# Routes

random_number = 3000


#Get Stats
@app.route('/api/items/<string:container_id>', methods=['GET'])
def get_stats(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    cpu_stats = container.stats(stream=False)
    cpu_usage = cpu_stats['cpu_stats']['cpu_usage']['total_usage'] / cpu_stats['cpu_stats']['system_cpu_usage'] * 100
    memory_usage = cpu_stats['memory_stats']['usage']/ 1024**2
    total_memory = container.attrs['HostConfig']['Memory'] / 1024**3
    network_io = [cpu_stats['networks']['eth0']['rx_bytes'] / 1024, cpu_stats['networks']['eth0']['tx_bytes'] / 1024**2]

    print(cpu_usage)
    print(memory_usage)
    print(total_memory)
    print(network_io)

    return jsonify(cpu_stats)

#Given a repo link, host it
@app.route('/api/create_website', methods=['POST'])
def create_item():
    global random_number
    data = request.json    
    repo_url = data.get('rep_url')
    repo_name = re.search(r'\/([^\/]+)\/?$', repo_url).group(1).lower()
    container_name = f"{repo_name}_container".lower()
    image_tag = f"{repo_name}_image".lower()
    port_mapping = f"127.0.0.1:{random_number}:{random_number}"  # You can adjust this as needed
    random_number += 1
    bash_script =  f"""#!/bin/bash
    
# Variables
REPOSITORY_NAME="{repo_name}" # Name your local Docker image
IMAGE_TAG="{image_tag}" # Tag for your Docker image
GITHUB_REPO_URL="{repo_url}" # GitHub Repository URL
CONTAINER_NAME="{container_name}" # Name for your local container
PORT_MAPPING="{port_mapping}" # Local:Container port mapping (adjust as needed)
    
# Clone the GitHub repository
git clone $GITHUB_REPO_URL repo_dir
cd repo_dir
    
# Build your Docker image (assuming the Dockerfile is in the root of the repo)
docker build -t $REPOSITORY_NAME:$IMAGE_TAG .
    
# Run your Docker container
docker run -d --name $CONTAINER_NAME -p $PORT_MAPPING $REPOSITORY_NAME:$IMAGE_TAG
    
# Clean up (optional)
cd ..
rm -rf repo_dir
    """
    
    # Write the bash script to a temporary file
    with open('temp_script.sh', 'w') as f:
        f.write(bash_script)
    
    # Set execute permissions
    subprocess.run(['chmod', '+x', 'temp_script.sh'])
    
    # Execute the bash script
    subprocess.run(['./temp_script.sh'])

    return jsonify("Hello"), 201

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        item.update(request.json)
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return jsonify({"message": "Item deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
