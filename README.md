# SAM_MODEL-FASTAPI-APP

This project is a web application designed to perform image segmentation using the Segment Anything Model (SAM). The application allows users to upload images, process them through the SAM, and visualize the segmentation results directly on the webpage. The app is built with FastAPI for the backend and served using Docker for easy deployment.

Features :

Image Upload: Users can upload images through the web interface.
Image Segmentation: The uploaded images are segmented using the SAM model.
Result Display: The segmented images are displayed on the same web interface.
Dockerized Deployment: The application can be easily deployed using Docker.

You can also run the app as a container from the docker hub
To pull the image you can following command : docker pull shyamshanckin/fastapi-sam-app:latest


Technologies Used

FastAPI: A modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
Docker: A platform used to develop, ship, and run applications inside containers, which are isolated environments that can contain all the necessary dependencies.
Segment Anything Model (SAM): A pre-trained image segmentation model used to perform the segmentation tasks.


