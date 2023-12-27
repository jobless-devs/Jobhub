# Docker and Docker-Sync Development Guide

## Initial Setup
```bash
# Install Docker and Docker-Compose (macOS using Homebrew)
brew install docker docker-compose

# Install docker-sync
gem install docker-sync

# Clone Repositories
git clone https://github.com/jobless-devs/Jobhub.git 
```

## Running Your Development Environment
```bash
# where docker-sync.yml is located, start docker-sync
cd Jobhub/dev 
docker-sync start

# Start Services with Docker-Compose
docker-compose up
```

## Making and Testing Changes
```bash
# Make Changes in your `client` and `scraper` code

# Rebuild Containers (if needed)
# cd path/to/docker-compose-directory
docker-compose up --build

# Test Changes
# Access the client service at localhost:3000 and Postgres at localhost:5432

# Debugging
docker-compose logs
```