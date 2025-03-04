FROM python:3.12
# Set the working directory inside the container
WORKDIR /app
# Ensure Python finds `customers` as a package
ENV PYTHONPATH=/app
# Copy requirements and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

## Expose the port (if needed)
EXPOSE 8001
#
## Run the application (modify this based on your framework, e.g., Flask, FastAPI)
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8001"]
