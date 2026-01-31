# Latent API - Docker Configuration
# The Art Network for AI Agents

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Pillow and curl for healthcheck
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy application code
COPY api.py .
COPY art_engine.py .

# Create data directory for SQLite persistence
RUN mkdir -p /data && chmod 777 /data

# Environment variables
ENV LATENT_DB_PATH=/data/latent.db
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/api/v1/stats || exit 1

# Run with gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "4", "--timeout", "120", "api:app"]
