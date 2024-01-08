#!/bin/bash

# Name of the Docker image and container
IMAGE_NAME="jobhub-scraper-image"
CONTAINER_NAME="jobhub-scraper-container"

# Always rebuild the Docker image to ensure it's up-to-date
echo "Building/Rebuilding Docker image: $IMAGE_NAME"
docker build -t $IMAGE_NAME .

# Check if a container with the same name is already running
RUNNING_CONTAINER=$(docker ps -q -f name=$CONTAINER_NAME)

if [ -n "$RUNNING_CONTAINER" ]; then
    echo "Stopping existing container: $CONTAINER_NAME"
    docker stop $CONTAINER_NAME
fi

# Run the Docker container
echo "Running Docker container: $CONTAINER_NAME"
docker run --name $CONTAINER_NAME $IMAGE_NAME
# if you want to run the container in the background, use the following command instead:
# docker run -d --name $CONTAINER_NAME $IMAGE_NAME



echo "Container $CONTAINER_NAME finished running"



# Stop and remove the container
echo "Stopping and removing container: $CONTAINER_NAME"
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME

# Optional: Remove the Docker image
# Uncomment the following line if you want to remove the image as well
# docker rmi <image-name or image-id>

echo "Container $CONTAINER_NAME has been stopped and removed"