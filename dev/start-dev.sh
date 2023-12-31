#!/bin/bash

# Function to start docker-sync
start_docker_sync() {
  echo "Starting docker-sync..."
  docker-sync start
}

# Function to build docker-compose
build_docker_compose() {
  echo "Building docker-compose..."
  docker-compose build
}

# Function to run Docker containers
run_docker_containers() {
  echo "Running Docker containers..."
  docker-compose up -d
  echo "Setup is complete! Your Docker environment is up and running."
  echo "To stop, please run: source stop-dev.sh"
}

# Main script
# check_prerequisites
source prerequisites.sh
start_docker_sync
build_docker_compose
run_docker_containers
