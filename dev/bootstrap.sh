#!/bin/bash

# Determine which shell profile to use (.bash_profile for bash and .zshrc for zsh)
SHELL_PROFILE="$HOME/.bash_profile"
if [ "$SHELL" = "/bin/zsh" ]; then
    SHELL_PROFILE="$HOME/.zshrc"
elif [ "$SHELL" = "/bin/bash" ]; then
    SHELL_PROFILE="$HOME/.bash_profile"
fi

# Install Homebrew Ruby
echo "Installing Homebrew Ruby..."
brew install ruby

# Update PATH to include Homebrew Ruby and Gem Executable Directory
echo 'export PATH="/usr/local/opt/ruby/bin:/usr/local/lib/ruby/gems/3.2.0/bin:$PATH"' >> "$SHELL_PROFILE"

# Reload Shell Configuration
echo "Updating and sourcing the shell profile..."
source "$SHELL_PROFILE"

# Verify Ruby Version
echo "Verifying Ruby version..."
ruby -v

# Install docker-sync
echo "Installing docker-sync..."
gem install docker-sync

# Verify docker-sync Installation
echo "Verifying docker-sync installation..."
docker-sync -v

# Start docker-sync
echo "Starting docker-sync..."
docker-sync start

# Run Docker containers as defined in the docker-compose.yml file
echo "Running Docker containers..."
docker-compose up -d

echo "Setup is complete! Your Docker environment is ready."
echo "To start your Docker containers: docker-compose up"
echo "To stop your Docker containers: docker-compose down"
echo "To clean up resources: docker system prune"
