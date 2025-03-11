#!/bin/sh
set -e

echo "Waiting for Postgres to become ready..."

# Loop until Postgres is ready to accept connections
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
    echo "$DB_HOST $DB_PORT $DB_USER"
    echo "Postgres is unavailable - sleeping"
    sleep 2
done

echo "Postgres is up - running migrations..."
alembic upgrade head

echo "Starting FastAPI application..."
exec uvicorn app.main:app --reload --host 0.0.0.0 --port 8001


