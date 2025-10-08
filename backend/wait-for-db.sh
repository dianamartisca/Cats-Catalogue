#!/bin/sh
set -e

host="${DATABASE_HOST:-localhost}"
port="${DATABASE_PORT:-5432}"
max_attempts=${MAX_DB_ATTEMPTS:-60}
attempt=1

echo "Waiting for database at ${host}:${port} (max ${max_attempts} attempts)"
while ! nc -z $host $port; do
  echo "Attempt ${attempt}/${max_attempts}: DB not ready yet"
  attempt=$((attempt+1))
  if [ $attempt -gt $max_attempts ]; then
    echo "Timed out waiting for DB after ${max_attempts} attempts"
    exit 1
  fi
  sleep 1
done

echo "Database is up"
