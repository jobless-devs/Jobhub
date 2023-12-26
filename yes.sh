#!/bin/bash

# Install Homebrew Ruby
echo "Installing Homebrew Ruby..."
brew install ruby

# Update PATH to include Homebrew Ruby
echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> ~/.zshrc

# Reload Shell Configuration
source ~/.zshrc

# Verify Ruby Version
echo "Verifying Ruby version..."
ruby -v

# Install docker-sync
echo "Installing docker-sync..."
gem install docker-sync

# Add Gem Executable Directory to PATH
echo 'export PATH="/usr/local/lib/ruby/gems/3.2.0/bin:$PATH"' >> ~/.zshrc

# Reload Shell Configuration Again
source ~/.zshrc

# Verify docker-sync Installation
echo "Verifying docker-sync installation..."
docker-sync -v

# Start docker-sync
echo "Starting docker-sync..."
docker-sync start

# Run Docker containers as defined in the docker-compose.yml file
echo "Running Docker containers..."
docker-compose up -d