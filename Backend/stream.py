import matplotlib.pyplot as plt
import docker

def visualize(stream):
    for stats in stream:
        print(stats)

if __name__ == "__main__":
    client = docker.from_env()
    container = client.containers.get("499731b3472a44680fbcfe965956fa789a5884232ebdc804462d9e443fa0130a")
    stream = container.stats(stream=True)
    visualize(stream)