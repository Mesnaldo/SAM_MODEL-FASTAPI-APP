# SAM_MODEL-FASTAPI-APP

This project is a web application designed to perform image segmentation using the Segment Anything Model (SAM). The application allows users to upload images, process them through the SAM, and visualize the segmentation results directly on the webpage. The app is built with **FastAPI** for the backend and served using **Docker** for easy deployment.

## Features

- **Image Upload**: Users can upload images through the web interface.
- **Image Segmentation**: The uploaded images are segmented using the **Segment Anything Model (SAM)**.
- **Result Display**: The segmented images are displayed on the same web interface.
- **Dockerized Deployment**: The application can be easily deployed using Docker.

## Quick Start

You can run the app as a container from Docker Hub. To pull the image, use the following command:

```bash
docker pull shyamshanckin/fastapi-sam-app:latest



