# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies (make sure requirements.txt exists in your project)
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside the container (if you're running a web server)
EXPOSE 5000

# Define environment variable (optional, for example Flask)
ENV FLASK_APP=app.py

# Run the application (this will vary depending on your project setup)
CMD ["python", "app.py"]
