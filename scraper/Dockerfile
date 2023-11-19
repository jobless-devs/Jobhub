# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements.txt file to use Docker's caching mechanism
COPY requirements.txt ./

# Install packages in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application's code
COPY . .

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set the entrypoint script to be executed
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]