#!/bin/bash
# Run your main application
echo "Running scraper"
# this command will run the scraper, but it will not keep the container running
# for development purposes, we don't need to run the scraper every time we run the container
python /opt/jobhub-scraper/main.py


# Then keep the container running
# tail -f /dev/null
echo "Scraper container finished running" 
