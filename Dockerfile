# Use an official lightweight Python runtime
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code, tests, and data folders into the container
COPY . .

# Run your main script when the container starts
CMD ["python", "main.py"]
