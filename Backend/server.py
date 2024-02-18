from flask import Flask, jsonify, request, Response, stream_with_context, json
import docker
import subprocess
import os
import re
import random
from util  import  get_container_stats
from flask_cors import CORS, cross_origin
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import docker
import time
import logging
from util import get_container_stats
import slack
import os
from pathlib import Path
# from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

from LLM import reportGeneration
from LLM import generated_script

app = Flask(__name__)
cors = CORS(app)


# Sample data
data = [
    {"id": 1, "name": "Item 1", "description": "Description of Item 1"},
    {"id": 2, "name": "Item 2", "description": "Description of Item 2"},
    {"id": 3, "name": "Item 3", "description": "Description of Item 3"}
]



# Routes

random_number = random.randint(3000, 4999)

def trigger_alert(text):
  """
  Sends a message to a specific channel on Slack.

  Args:
    channel_id: The ID of the Slack channel to send the message to.
    text: The text of the message to send.
  """

  channel_id = '#random'

  # Load the access token securely
  token = 'xoxb-6657086214227-6659740333668-H1fBtRRXIOaqiZ73CdapR28o'

  # Use the WebClient for sending messages
  client = slack.WebClient(token=token)

  # Send the message and handle potential errors
  try:
    client.chat_postMessage(channel=channel_id, text=text)
    print(f"Message sent to channel: {channel_id}")
  except slack.errors.SlackApiError as e:
    print(f"Error sending message: {e}")

def check_container_status(container_name, metrics, metrics_threshold):
  # Get CPU and memory stats
  stats = get_container_stats(container_name)

  # Check thresholds and trigger alerts
  triggered = False
  for i in range(len(metrics)):
    if stats[metrics[i]] > metrics_threshold[i]:
      logging.warning(f"Container {container_name} {metrics[i]}: {stats[metrics[i]]:.2f}%, exceeding threshold of {metrics_threshold[i]}")
      trigger_alert("Some Usage High")
      triggered = True

  return triggered

#Get Stats
@app.route('/api/items/<string:container_id>', methods=['GET'])
def get_stats(container_id):
    # client = docker.from_env()
    # container = client.containers.get(container_id)
    # cpu_stats = container.stats(stream=False)
    # cpu_usage = cpu_stats['cpu_stats']['cpu_usage']['total_usage'] / cpu_stats['cpu_stats']['system_cpu_usage'] * 100
    # memory_usage = cpu_stats['memory_stats']['usage']/ 1024**2
    # total_memory = container.attrs['HostConfig']['Memory'] / 1024**3
    # network_io = [cpu_stats['networks']['eth0']['rx_bytes'] / 1024, cpu_stats['networks']['eth0']['tx_bytes'] / 1024**2]



    return jsonify(get_container_stats(container_id))

#Given a repo link, host it
@app.route('/api/create_website', methods=['POST'])
def create_item():
    global random_number
    data = request.form.get('rep_url')
    repo_url = data
    repo_name = re.search(r'\/([^\/]+)\/?$', repo_url).group(1).lower() + str(random_number)
    container_name = f"{repo_name}".lower()
    image_tag = f"{repo_name}_image".lower()
    port_mapping = f"127.0.0.1:{random_number}:{random_number+5}"  # You can adjust this as needed
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

if [ ! -f Dockerfile ]; then
    echo "Dockerfile not found, adding one..."
    cat << EOF > Dockerfile
{generated_script}
fi
    
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
    subprocess.run(['chmod', '+x', 'temp_script.sh'],shell=True)
    
    # Execute the bash script
    subprocess.run(['temp_script.sh'],shell=True)

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


# @app.route('/api/send_mail', methods = ["POST"])
# def send_email():
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587
#     smtp_username = 'vm5503@gmail.com'
#     smtp_password = 

#     data = request.json

#     to_email = data.get('to_email')
#     subject = data.get('subject')
#     body = data.get('body')
#     attachment = data.get('attachment')

#     msg = MIMEMultipart()
#     msg['From'] = smtp_username
#     msg['To'] = to_email
#     msg['Subject'] = subject

#     msg.attach(MIMEText(body, 'plain'))

#     if attachment:
#         with open(attachment, 'rb') as file:
#             attach_part = MIMEApplication(file.read(), Name=attachment)
#         attach_part['Content-Disposition'] = f'attachment; filename="{attachment}"'
#         msg.attach(attach_part)

#     try:
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.ehlo()
#         server.starttls()
#         server.ehlo()
#         server.login(smtp_username, smtp_password)
#         server.sendmail(smtp_username, to_email, msg.as_string())
#         server.quit()
#         print(f"Email sent to {to_email}")
#         return jsonify("Asian"), 201
#     except Exception as e:
#         print(f"Failed to send email to {to_email}: {str(e)}")
#         return jsonify("Not Asian"), 201
    

@app.route('/api/getAll', methods=['GET'])
def getAll():
    client = docker.from_env()
    containers = client.containers.list()


    container_ids = [{'status':container.status,
                      'id':container.id, 
                      'name': container.name, 
                      'created': container.attrs['Created']} for container in containers]
    print(container_ids)
    response_data = {
    "container_ids": container_ids,
    "container_count": len(containers)
    }
    return jsonify(response_data)

@app.route('/api/getLog/<string:container_id>', methods=['GET'])
def getLog(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    logs = container.logs()
    ls = logs.decode('utf-8').split('\n')
    logs_json = {'logs': ls,
                 'id': container.id,
                 'name': container.name,
                 'status': container.status}
    return logs_json

@app.route('/api/create_report/<string:container_id>', methods=['GET'])
def create_report(container_id):
    return jsonify(reportGeneration(getLog(container_id)))

if __name__ == '__main__':
    app.run(debug=True)
