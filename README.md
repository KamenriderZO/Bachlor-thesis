# Framework for evaluating the trustworthiness of anomaly detection inautonomous vehicles simulator
## Introduction
The code framework is based on an open source urban autonomous driving simulator called Carla.<br>
You can found it here : https://github.com/carla-simulator/carla/releases <br>
Note : The code frame work is using Carla version 0.9.13.Maybe there is already new version published.
To avoid compatibility problem 0.9.13 is recommended.
About how to setup Carla : https://carla.readthedocs.io/en/latest/start_quickstart/ <br>
In Carla simulator there will be well made vehicle modules, road conditions, walkers as NPCs...<br>
It almost fullfilled the need of a user,who want to simulate auto driving cars and oberserve them.<br>
The framework is used to research the human trust worthiness on the anomaly detection part of the AI system in autonomous vehicles.<br>
It will generate and detect some vehicle anomalies like "door not closed","Engine problems"...<br>
In reality the vehicle sensors and AI sometimes make mistakes.Will you trust the information that it feed backs to you?<br>
Too much trust on a poor designed AI system or detector is a bad idea.Of cause not trust them at all is also a waste of hardware!<br>
To evaluate the human trust worthiness is the core of the code work.

## Requirements
<strong>System requirements:</strong> CARLA is built for Windows and Linux systems.<br>
<strong>An adequate GPU:</strong> CARLA aims for realistic simulations, so the server needs at least a 6 GB GPU although we would recommend 8 GB. A dedicated GPU is highly recommended for machine learning.<br>
<strong>Disk space:</strong> CARLA will use about 20 GB of space.<br>
<strong>Python:</strong> Python is the main scripting language in CARLA. CARLA supports Python 2.7 and Python 3 on Linux, and Python 3 on Windows.<br>
<strong>Pip:</strong> Some installation methods of the CARLA client library require pip or pip3 (depending on your Python version) version 20.3 or higher.<br>
<strong>Two TCP ports and good internet connection:</strong> 2000 and 2001 by default. Make sure that these ports are not blocked by firewalls or any other applications.<br>
<strong>Other requirements:</strong> CARLA requires some Python dependencies. Install the dependencies according to your operating system.

## Installation
Install Pygame<br>
pip install --user pygame numpy<br>
Install client library<br>
pip install carla<br>
Download Carla 0.9.13 package and unzip it. https://github.com/carla-simulator/carla/releases <br>
Download Carla additional maps package. The address is the same as above. Unzip them and override folders.<br>
Download my release pack and unzip the file into the same directory as Carla.

## How to use
First launch CarlaUE4.exe. This may take some time the first time.If you can't start Carla the problem maybe your environment can't launch UE.<br>
Firstly download Epic games and install Unreal Engine 4.<br>
<br>
After a bit seconds you will see a window with an empty map.Try use W,A,S,D to move the camera.<br>
Hold your mouse right button and drag it will change the camera view.<br>
When the map is loaded means the Carla server is initialized and ready for client's connection.<br>
launch the run.bat to start the scenario controller.<br>
Input the parameters you like and enjoy the autonomous driving simulation with anomaly detections.<br>
During the simulation series of anomalies will appear or not.Try to pressed the related buttons to decide if you want to ignore it or take action.<br>
After the simulation find the log folder and check the log files.

## Parameter settings
### Scenario
There are 4 predesigned scenarios .You must seletct one of them to start the simulation.
### Map 
Different Scenario binds different map choices.Read the scenario description in the info panel.<br>
Town04 and Town06 are highway maps,which are much bigger files than others.
### Simulation time
Input from 5~20 decides how long the simulation will last.
### Weathers
To change the weather in Carla.It will some how influence your sight.
### Traffic situation
This decides how many NPCs will be generated in the map.
### Anomaly generation rate
The anomaly is generated every tick. Higher value means more frequently generated and detected.
### False positive rate
This is a part of accuracy of the anomaly detection.Higher value means worse accuracy.<br>
This means how frequently a fake signal light will be given.(Normal vehicle but fake anomaly)
### False negative rate
This is a part of accuracy of the anomaly detection.Higher value means worse accuracy.<br>
This means how possible if an anomaly is generated but the detector didn't notice that.(Abnormal vehicle but no signal light)