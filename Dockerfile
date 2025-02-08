# Use a stable Python version (3.10 recommended)
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Ensure Python finds `authentication` as a package
ENV PYTHONPATH=/app

# Install system dependencies (for distutils in Python 3.12+)
RUN apt-get update && apt-get install -y python3-distutils && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install setuptools early to avoid distutils issues
RUN pip install --no-cache-dir --upgrade pip setuptools

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Ensure `uvicorn` is installed (in case it's missing from requirements.txt)
RUN pip install --no-cache-dir uvicorn

# Expose the application port
#EXPOSE 8001
#
## Run the application using Uvicorn
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
