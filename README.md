# TCSS 506 Assignment 2
For the second assignment in TCSS 506 I developed a demo Flask Application. The demo application was deployed on an Amazon Web Service EC2 via Docker. 

The application has two API endpoints. 
* (`/your_name`) prints a message saying "Hello World from Sean". 
* (`/datetime`) prints a message with the current date and time. 

## Building The Docker Image
To build the image and publish the updated image to docker hub. 

```bash
docker build -t flask-app .
docker push warlicks/flask-app:latest
```

## Deploying the App Via Docker
To start the application run the following commands
```bash
docker pull warlicks/flask-app
docker run -rm -d -p 5000:5000 warlicks/flask-app
```