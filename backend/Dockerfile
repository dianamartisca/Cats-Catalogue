FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps for building some Python packages and runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    curl \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt
RUN pip install --no-cache-dir gunicorn

# Copy application code
COPY . /app

# Make wait script executable
RUN chmod +x /app/wait-for-db.sh

# Expose port used by the app
EXPOSE 5000

# Start: wait for DB, then run gunicorn
CMD ["/bin/sh", "-c", "./wait-for-db.sh && gunicorn --workers 3 --bind 0.0.0.0:5000 app:app"]
