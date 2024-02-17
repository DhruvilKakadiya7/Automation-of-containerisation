import docker

client = docker.from_env()
for event in client.events(filters={"container": "499731b3472a44680fbcfe965956fa789a5884232ebdc804462d9e443fa0130a", "type": "container"}):
    print(event)
    if event["status"] == "die":  #check for "oom" "exec_create_failed", and a lot more stuff check docs
        print(f"Error event: {event}")