from flask import Flask, jsonify, request
import docker
import subprocess


app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "Item 1", "description": "Description of Item 1"},
    {"id": 2, "name": "Item 2", "description": "Description of Item 2"},
    {"id": 3, "name": "Item 3", "description": "Description of Item 3"}
]

# Routes


#Get Stats
@app.route('/api/items/<string:container_id>', methods=['GET'])
def get_stats(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    cpu_stats = container.stats(stream=False)
    return jsonify(cpu_stats)

#Given a repo link, host it
@app.route('/api/items', methods=['POST'])
def create_item():

    subprocess.run(['chmod', '+x', 'temp_script.sh'])
    subprocess.run(['./temp_script.sh'])
    
    new_item = request.json

    data.append(new_item)
    return jsonify(new_item), 201

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
