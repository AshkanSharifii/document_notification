# syntax=docker/dockerfile:1

#########################
# 1) Builder stage
#########################
FROM python:3.12-bookworm AS builder

# Prevent Python from writing .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install build tools (for any compiled dependencies)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install into the default location
COPY prod.requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r prod.requirements.txt

# Copy the rest of the application code
COPY . .

#########################
# 2) Final stage
#########################
FROM python:3.12-bookworm

# Build‐time arg to choose environment (dev or prod)
ARG APP_ENV=prod

ENV APP_ENV=${APP_ENV} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="/app"

# Create a non‐root user and group
RUN addgroup --system appgroup && \
    adduser  --system --ingroup appgroup appuser

# Ensure /app exists and is owned by the non‐root user
WORKDIR /app
RUN mkdir -p /app && chown -R appuser:appgroup /app

# Copy installed Python packages and console scripts from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin             /usr/local/bin

# Copy application code from builder, then re‐chown
COPY --from=builder /app /app
RUN chown -R appuser:appgroup /app

# Switch to non‐root user
USER appuser

# Expose FastAPI port
EXPOSE 5000

# Start FastAPI via Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]
