# Use a minimal Python base image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install system dependencies (for tgcrypto, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your bot source code
COPY . .

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Start the bot
CMD ["python3", "-m", "AfkRobot"]