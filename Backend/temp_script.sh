#!/bin/bash
    
# Variables
REPOSITORY_NAME="dockertest" # Name your local Docker image
IMAGE_TAG="dockertest_image" # Tag for your Docker image
GITHUB_REPO_URL="https://github.com/BakuDoriya-KatsZuku/DockerTest" # GitHub Repository URL
CONTAINER_NAME="dockertest_container" # Name for your local container
PORT_MAPPING="127.0.0.1:3000:3000" # Local:Container port mapping (adjust as needed)
    
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
    