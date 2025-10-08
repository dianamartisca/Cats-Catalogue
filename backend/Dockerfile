FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    curl \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt
RUN pip install --no-cache-dir gunicorn

COPY . /app

RUN chmod +x /app/wait-for-db.sh

EXPOSE 5000

CMD ["/bin/sh", "-c", "./wait-for-db.sh && gunicorn --workers 3 --bind 0.0.0.0:5000 app:app"]
