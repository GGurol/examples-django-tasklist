# RULE 1: Always use Python 3.12
FROM python:3.12-slim

# Set environment variables (with English comments)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system-level dependencies required for packages like psycopg
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# --- ADDED STEP: Upgrade pip to the latest version ---
RUN python -m pip install --upgrade pip

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project code
COPY . .