#!/bin/bash

# Function to check if a command is available
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Function to stop docker-sync
stop_docker_sync() {
  if command_exists docker-sync; then
    echo "Stopping docker-sync..."
    docker-sync stop
  else
    echo "docker-sync is not installed, skipping"
  fi
}

# Function to stop Docker containers
stop_docker_containers() {
  if command_exists docker; then
    echo "Stopping Docker containers..."
    docker stop $(docker ps -a -q)
  else
    echo "Docker is not installed, skipping"
  fi
}

# Main script
stop_docker_sync
stop_docker_containers
