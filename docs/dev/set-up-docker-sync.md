## Environment Setup for docker-sync on macOS
`docker-sync` optimizes file synchronization between host and Docker containers, crucial for macOS/Windows where native Docker mounts are slow. It enhances file access speed, crucial for projects with frequent file operations, offering a more efficient alternative to standard Docker volume mounts.

```bash
# Install Homebrew Ruby
brew install ruby

# Update PATH to include Homebrew Ruby
echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> ~/.zshrc

# Reload Shell Configuration
source ~/.zshrc

# Verify Ruby Version
ruby -v

# Install docker-sync
gem install docker-sync

# Add Gem Executable Directory to PATH
echo 'export PATH="/usr/local/lib/ruby/gems/3.2.0/bin:$PATH"' >> ~/.zshrc

# Reload Shell Configuration Again
source ~/.zshrc

# Verify docker-sync Installation
docker-sync -v

# Start docker-sync
docker-sync start
