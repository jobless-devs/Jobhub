#!/bin/bash
# Run your main application
python /app/main.py

# Then keep the container running
tail -f /dev/null
