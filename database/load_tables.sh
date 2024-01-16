#!/bin/bash

# PURPOSE: 
# Loading tables before running a scraper. Assumes that the PostgreSQL 
# container is already running 

# Load the environment variables from the .env file
# The script checks for the presence of a .env file in the same directory. 
# This file should contain necessary environment variables like DB_USER, DB_NAME, etc.
if [ -f .env ]; then
    export $(cat .env | xargs)
else
    echo ".env file not found"
    exit 1
fi

# Configuration
CONTAINER_NAME="jobhub-postgres" 
SQL_FILE="load_tables.sh" 

# Step 1: Copy the SQL file to the container
# This step copies the SQL file from the host to the Docker container.
echo "Copying SQL file to the container..."
docker cp $SQL_FILE $CONTAINER_NAME:/$SQL_FILE

# Step 2: Execute the SQL file
echo "Executing SQL file..."
docker exec -u $DB_USER $CONTAINER_NAME psql -d $DB_NAME -f /$SQL_FILE

echo "SQL file executed successfully."
