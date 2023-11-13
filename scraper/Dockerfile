# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy only the requirements.txt file to use Docker's caching mechanism
COPY requirements.txt ./

# Install packages in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application's code
COPY . .

# Run main.py when the container launches 
CMD ["python", "./main.py"] 