
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
# from slack_bolt import App
import subprocess


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = slack.WebClient("xoxb-6657086214227-6659740333668-H1fBtRRXIOaqiZ73CdapR28o")
BOT_ID = client.api_call("auth.test")['user_id']

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events',app)

@slack_event_adapter.on('message')
def message(payload):
    print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if ';' not in text:
        return
    # 
    if 'showall' in text:
        text = 'showall'
    elif "restart" in text:
        container_id = text.split(" ")[-1]

        bash_script = f"""# Restart the Docker container

CONTAINER_ID = "{container_id}"
docker restart "$CONTAINER_ID"

# Check if the restart was successful
if [ $? -eq 0 ]; then
    echo "Container $CONTAINER_ID restarted successfully."
else
    echo "Failed to restart container $container_id."
fi"""
        
        with open('restart_container.sh', 'w') as f:
            f.write(bash_script)
            
        # Set execute permissions
        subprocess.run(['chmod', '+x', 'restart_container.sh'],shell=True)
        
        # Execute the bash script
        subprocess.run(['restart_container.sh'],shell=True)

    elif "stop" in text:
        container_id = text.split(" ")[-1]

        bash_script = f"""# Restart the Docker container

CONTAINER_ID = "{container_id}"
docker stop "$CONTAINER_ID"

# Check if the stop was successful
if [ $? -eq 0 ]; then
    echo "Container $container_id stopped successfully."
else
    echo "Failed to stop container $container_id. Check if the container ID is valid and the container is running."
fi"""
        
        # from docker import Docker

        # # Replace with your Docker daemon endpoint and container ID
        # client = Docker(base_url="unix://var/run/docker.sock")
        # container_id = "your_container_id"

        # # Start the container
        # client.containers.start(container_id)
        # client.containers.stop(container_id)

        # print(f"Container {container_id} started successfully")
        
        with open('restart_container.sh', 'w') as f:
            f.write(bash_script)
            
        # Set execute permissions
        subprocess.run(['chmod', '+x', 'restart_container.sh'],shell=True)
        
        # Execute the bash script
        subprocess.run(['restart_container.sh'],shell=True)

    if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text = text)



if __name__ == '__main__':
    app.run(debug=True)
