# Use a more recent Anaconda base image
FROM continuumio/anaconda3:latest

# Copy the current folder structure and content to the /usr/ML/app directory in the container
COPY . /usr/ML/app

# Expose port 5000 for the Flask application
EXPOSE 5000

# Set the current working directory to the root directory
WORKDIR /usr/ML/app

#Install the required libraries
RUN pip install -r requirements.txt

# Define the command to run when the container starts
CMD python flask_api.py



