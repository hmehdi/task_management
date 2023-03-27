# Base image
FROM node:14.17.5 AS build

# Set the working directory
WORKDIR /app

# Copy frontend files to working directory
COPY frontend/package.json frontend/package-lock.json ./

# Install frontend dependencies
RUN npm install

# Copy frontend source code
COPY frontend ./

# Build the frontend
RUN npm run build --prod

# Use the official Python image as parent image
FROM python:3.8.12-bullseye

# Create and set the working directory
WORKDIR /app

# Copy Django and backend files to working directory
COPY requirements.txt manage.py ./
COPY backend backend

# Install backend dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the built frontend files to Django's static directory
COPY --from=build /app/dist/frontend/static/ /app/backend/static/

# Expose port 8000 for Django development server
EXPOSE 8000

# Run Django development server with manage.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# To run the project inside a container:

# 1. Build a Docker image using the Dockerfile:
     #  docker build -t task-management .
     
# 2. Run a Docker container based on the built image:
     #  docker run -p 8000:8000 task-management