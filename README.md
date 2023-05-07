# EE250 Project

## Team Members
- team member 1: Ishraq Rahman
- team member 2: Carrie Lei

Link to our Video Demo: 
https://drive.google.com/drive/folders/1Ju48B9d3jF7ujeGPnRrjpIHEtJ0Jq3l4?usp=sharing

Link to Project Write-Up:
https://docs.google.com/document/d/1WSx-mhx1qgWUKyjlRXH-mfjNvMAqR-yDcCq0VRLwhD8/edit

-------------------------------------------------------------

Project Description:
This project is our EE250 final project assignment.

By reflecting the ideology of node to node communication, we're going to use
one of our previous projects that contained grovepi sensors and Dexter industries
to develop our weather stylist where we have a sensor measuring temperature and humidity
and collect data. We will be using our RapsberryPi and laptop to have them communicate 
with each other as data is being collected through our sensor.

To run the interactive prediction model, make sure to run the Jupyter notebook titled "tempPrediction.ipynb"
after downloading the "LosAngelesTempData.csv" into the same directory. This data was trimmed from 
a larger dataset found from Kaggle here:
https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data?resource=download .

---------------------------------------------------------------

Instruction Manual:

Python libraries used:
- grovepi 
- grove_rgb_lcd 
- time 
- math 
- numpy
- matplotlib
- pandas
- sklearn (linear_model & LinearRegression)

We have used one source as a reference to implement code of the weather 
station and have both RaspberryPi and our local device (laptops) to 
communicate with each other as the temperature and humidity sensor 
collects data: 
https://www.dexterindustries.com/GrovePi/projects-for-the-raspberry-pi/raspberry-pi-temperature-sensor/

Physical Components Required:
- Raspberry PI 4
- GrovePi Shield
- GrovePi RGB LCD
- GrovePi Temperature/Humidity Sensor

You can refer to what ports are being used to connect the components 
on the GrovePi Shield through the ee250project.py file. You may also
use this python file to utilize our program that is meant for the 
RaspberryPi. 

For the predictive model, the user inputs four parameters (humidity, pressure, windspeed and month) 
and the program will return the predicted LA temperature (in Fahrenheit) given those conditions.

---------------------------------------------------------------
