#!/bin/bash
    
# Variables
REPOSITORY_NAME="dockertest4541" # Name your local Docker image
IMAGE_TAG="dockertest4541_image" # Tag for your Docker image
GITHUB_REPO_URL="https://github.com/BakuDoriya-KatsZuku/DockerTest" # GitHub Repository URL
CONTAINER_NAME="dockertest4541_container" # Name for your local container
PORT_MAPPING="127.0.0.1:4541:4541" # Local:Container port mapping (adjust as needed)
    
# Clone the GitHub repository
git clone $GITHUB_REPO_URL repo_dir
cd repo_dir

if [ ! -f Dockerfile ]; then
    echo "Dockerfile not found, adding one..."
    cat << EOF > Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000
EOF

fi
    
# Build your Docker image (assuming the Dockerfile is in the root of the repo)
docker build -t $REPOSITORY_NAME:$IMAGE_TAG .
    
# Run your Docker container
docker run -d --name $CONTAINER_NAME -p $PORT_MAPPING $REPOSITORY_NAME:$IMAGE_TAG
    
# Clean up (optional)
cd ..
rm -rf repo_dir
    