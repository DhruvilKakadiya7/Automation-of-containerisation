
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


def check_container_status(container_name, metrics, metrics_threshold):
  """
  Checks the CPU and memory usage of a container and triggers alerts if thresholds are exceeded.

  Args:
    container_name: Name of the docker container to monitor.
    cpu_threshold: CPU usage threshold percentage (int).
    memory_threshold: Memory usage threshold percentage (int).

  Returns:
    True if an alert was triggered, False otherwise.
  """

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


if __name__ == "__main__":
  # Replace with your actual container name and customize thresholds if needed
  container_name = "a58aef16262e9dc894c47fcb00fcbde923fd1df37252afc0e5e24091c4665003"

  # Set up logging
  logging.basicConfig(level=logging.WARNING)

  while True:
    triggered = check_container_status(container_name, ['cpu_usage'], [-10])
    if triggered:
      # Consider adding cooldown period to avoid repetitive alerts
      time.sleep(60)  # Wait for 1 minute before checking again
    else:
      time.sleep(5)  # Check every 5 seconds
