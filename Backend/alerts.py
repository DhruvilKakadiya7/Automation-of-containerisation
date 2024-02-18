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

app = Flask(__name__)
cors = CORS(app)


# Sample data
data = [
    {"id": 1, "name": "Item 1", "description": "Description of Item 1"},
    {"id": 2, "name": "Item 2", "description": "Description of Item 2"},
    {"id": 3, "name": "Item 3", "description": "Description of Item 3"}
]

# Routes

random_number = 3000

def send_email(to_email, subject, body, attachment):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'vm5503@gmail.com'
    smtp_password = 'zztm jcvd hlyj cxaz'

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment:
        with open(attachment, 'rb') as file:
            attach_part = MIMEApplication(file.read(), Name=attachment)
        attach_part['Content-Disposition'] = f'attachment; filename="{attachment}"'
        msg.attach(attach_part)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {str(e)}")

def trigger_alert(text):
  """
  Sends a message to a specific channel on Slack.

  Args:
    channel_id: The ID of the Slack channel to send the message to.
    text: The text of the message to send.
  """

  send_email("akhil07pc@gmail.com", "Docker Alert", text, None)

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

def check_container_status(container_name, metrics, metrics_threshold,name):
  # Get CPU and memory stats
  stats = get_container_stats(container_name)

  # Check thresholds and trigger alerts
  triggered = False
  for i in range(len(metrics)):
    if stats[metrics[i]] > metrics_threshold[i]:
      logging.warning(f"Container {name}: {container_name} \n {metrics[i]}: {stats[metrics[i]]:.2f}%, exceeding threshold of {metrics_threshold[i]}")
      trigger_alert(f"Container {name}: {container_name} \n {metrics[i]}: {stats[metrics[i]]:.2f}%, exceeding threshold of {metrics_threshold[i]}")
      triggered = True

  return triggered

@app.route('/api/alert', methods=['POST'])
def alert():
    name = request.form.get('name')
    id = request.form.get('id')
    metric = request.form.get('metric')
    threshold = request.form.get('threshold')
    print(name, id, metric, threshold)
    # Replace with your actual container name and customize thresholds if needed
    container_name = id

    # return jsonify(container_name)

    # Set up logging
    logging.basicConfig(level=logging.WARNING)

    while True:
        triggered = check_container_status(container_name, [metric], [int(threshold)], name)
        if triggered:
        # Consider adding cooldown period to avoid repetitive alerts
            time.sleep(60)  # Wait for 1 minute before checking again
        else:
            time.sleep(5)  # Check every 5 seconds
    
    return jsonify("Asian")

if __name__ == '__main__':
    app.run(debug=True,port=5001)
