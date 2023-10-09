# RefundItemClassification
# Table of Contents
  - [Overview](#overview)
  - [Technologies Used](#technologies-used)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [API Documentation](#api-documentation)
  - [Batch Processing](#batch-processing)
  - [Docker Containerization](#docker-containerization)
  - [Scheduling with GitHub Actions](#scheduling-with-github-actions)
  - [Security](#security)

## Overview
This is a simple API for classifying images using a pre-trained deep learning model, with a spotlight on batch processing. The API allows you to send a batch of images to be classified and receive predictions for each image in the batch.

## Technologies Used
- Python
- Flask
- TensorFlow
- Docker
- GitHub Actions

## Setup

### Prerequisites
- Python 3.6
- TensorFlow (for model inference)
- Docker (for containerization)
- GitHub Actions (for scheduling)

### Installation
1. Clone the repository:

```bash
git clone https://github.com/Oumaymabamoh/RefundItemClassification.git
```
3. Install the required Python packages:

``` bash 
pip install -r requirements.txt
```

2. Access the API at `http://localhost:5000`:
- The root path `/` provides a simple welcome message.
- The `/predict` route accepts POST requests with image files for classification.

### API Documentation
- **GET `/`**: Returns a welcome message.
- **POST `/predict`**: Accepts images for classification. Send a POST request with image files attached.

### Batch Processing
- The API supports batch processing of images. Place your image files in the `/test_data` directory.
- The daily cron job, scheduled using GitHub Actions, automatically triggers batch processing of new images every day at midnight (UTC).

### Docker Containerization
1. Build the Docker image:
docker build -t my-app

### Scheduling with GitHub Actions
- The project includes a GitHub Actions workflow (`cronjob.yml`) that runs a daily cron job to trigger the `/predict` endpoint and process new images.

### Security
- Ensure proper authentication and authorization mechanisms are in place to secure your API. Consider using API keys, tokens, or other authentication methods.

### Happy coding!
