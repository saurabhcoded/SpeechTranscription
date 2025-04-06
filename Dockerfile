# syntax=docker/dockerfile:1
FROM python:3.9.13-slim-buster

# Install system-level build tools and espeak
RUN apt-get update && \
    apt-get install -y \
    ffmpeg \
    g++ \
    make \
    build-essential \
    python3-dev \
    espeak && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /mozilla_tts

COPY requirements.txt .
RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt # No cache

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
