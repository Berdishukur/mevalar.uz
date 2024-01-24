# Pull the official base image
FROM python:3.9

# Set work directory
WORKDIR /code

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies

# Copy project
COPY . /code/
