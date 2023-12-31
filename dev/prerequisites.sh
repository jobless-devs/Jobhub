#!/bin/bash

# Function to check if a command is available
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Function to determine which shell profile to use (.bash_profile for bash and .zshrc for zsh)
get_shell_profile() {
  local shell_profile="$HOME/.bash_profile"
  if [ "$SHELL" = "/bin/zsh" ]; then
    shell_profile="$HOME/.zshrc"
  elif [ "$SHELL" = "/bin/bash" ]; then
    shell_profile="$HOME/.bash_profile"
  fi
  echo "$shell_profile"
}

# Function to install Ruby using rbenv
install_rbenv_and_ruby() {
  local ruby_version="3.2.2" # Replace with the desired version or a variable

  if command_exists ruby && [ "$(ruby -e 'print RUBY_VERSION')" = "$ruby_version" ]; then
    echo "Ruby $ruby_version is already installed."
  else
    echo "Installing Ruby $ruby_version..."
  
    command_exists brew || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew install rbenv ruby-build

    local shell_profile="$1"
    echo 'eval "$(rbenv init -)"' >> "$shell_profile"
    echo "Updating and sourcing the shell profile..."
    source "$shell_profile"

    rbenv install --verbose "$ruby_version"
    rbenv global "$ruby_version"
    rbenv rehash
  fi

  echo "Verifying Ruby version..."
  ruby -v
}

# Function to install docker-sync using gem
install_docker_sync() {
  if command_exists docker-sync; then
    echo "docker-sync is already installed. Skipping installation."
  else
    echo "Installing docker-sync..."
    gem install docker-sync
  fi
  echo "Verifying docker-sync installation..."
  docker-sync -v
}

# Function to check if Docker is installed and running
check_docker() {
  if command_exists docker; then
    echo "Docker is installed."
    if docker info >/dev/null 2>&1; then
      echo "Docker daemon is running."
    else
      echo "Error: Docker daemon is not running."
      exit 1
    fi
  else
    echo "Error: Docker is not installed. Please install Docker before continuing."
    exit 1
  fi
}

# Main script
SHELL_PROFILE=$(get_shell_profile)
install_rbenv_and_ruby "$SHELL_PROFILE"
install_docker_sync
check_docker
