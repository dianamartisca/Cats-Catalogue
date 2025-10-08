#!/bin/bash
set -euo pipefail

# --- Variables (customize these) ---
APP_DIR="/opt/devops-final-project"
USER="ubuntu"

echo "Starting instance1 setup"

# Update and install Docker
apt-get update -y
apt-get upgrade -y
apt-get install -y docker.io

# Create app directory
mkdir -p ${APP_DIR}
chown -R ${USER}:${USER} ${APP_DIR} || true

# Navigate to the directory containing docker-compose.yml
cd ${APP_DIR}

# Start the application using Docker Compose
docker-compose up -d
