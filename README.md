
# Pest-Pi

## Mission Statement
PestPi aims to introduce a revolutionary approach to pest management in agricultural settings, specifically tailored for farmers in Puerto Rico. The solution leverages advanced AI-based image processing technology to accurately identify common pests such as iguanas, boas, and rodents. By integrating a camera system that monitors designated areas for activity, PestPi will capture images upon detecting movement. It then sends the captured images to the MainPest which are then analyzed utilizing YOLOv8 to determine the presence of pests. Identified pests are then recorded and reported on a user-friendly dashboard, which provides real-time alerts and statistical data analysis to inform and empower farmers in their pest management efforts. This data-driven approach facilitates targeted interventions, promoting more sustainable farming practices. 

## Link to Project Webpage:

Link: https://sites.google.com/view/capstonepestpi/home

In our website you will find more information regarding our prototype such as:

- Elevator Pitch Video
- Presentation Slides
- Project Objectives

## Setting up for Use
To create the setup you're gonna need the following set up:

- A Raspberry Pi 
- A USB or Raspberry Pi compatible Camera
- A Virtual Machine setup with an FTP server and the AI model
- A Computer with the app.py running

## Running the Program
Open the terminal, change to the directory where the project is located and run the following
```bash
python app.py 

```

And open the browser in the following link: http://127.0.0.1:5000/
