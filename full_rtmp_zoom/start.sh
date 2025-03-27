#!/bin/bash

# Start NGINX in the background
nginx

# Give nginx a second to boot
sleep 1

# Start Python script
python /app/main.py

