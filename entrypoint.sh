#!/bin/sh
set -e

echo "Running Alembic migrations..."
# Run Alembic migrations (ensure alembic.ini is configured correctly)
alembic upgrade head

echo "Starting FastAPI application..."
exec uvicorn app.main:app --reload --host 0.0.0.0 --port 8001