#!/bin/bash
set -euo pipefail

APP_DIR="/opt/devops-final-project"
USER="ubuntu"
GIT_REPO="https://github.com/dianamartisca/DevOps-Final-Project.git"
BRANCH="main"

echo "Starting instance1 setup"

apt-get update -y
apt-get upgrade -y
apt-get install -y docker.io git

DOCKER_COMPOSE_VERSION="1.29.2"
curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

mkdir -p ${APP_DIR}
chown -R ${USER}:${USER} ${APP_DIR} || true

if [ ! -d "${APP_DIR}/.git" ]; then
  git clone --branch ${BRANCH} ${GIT_REPO} ${APP_DIR}
else
  cd ${APP_DIR}
  git fetch --all
  git reset --hard origin/${BRANCH}
fi

cd ${APP_DIR}

docker-compose up -d