# Framework for evaluating the trustworthiness of anomaly detection inautonomous vehicles simulator
## Introduction
The code framework is based on an open source urban autonomous driving simulator called Carla.
You can found it here : https://github.com/carla-simulator/carla/releases
Note : The code frame work is using Carla version 0.9.13.Maybe there is already new version published.
To avoid compatibility problem 0.9.13 is recommended.
About how to setup Carla : https://carla.readthedocs.io/en/latest/start_quickstart/
In Carla simulator there will be well made vehicle modules, road conditions, walkers as NPCs...
It almost fullfilled the need of a user,who want to simulate auto driving cars and oberserve them.

## Requirements
<strong>System requirements:</strong> CARLA is built for Windows and Linux systems.
<strong>An adequate GPU:</strong> CARLA aims for realistic simulations, so the server needs at least a 6 GB GPU although we would recommend 8 GB. A dedicated GPU is highly recommended for machine learning.
<strong>Disk space:</strong> CARLA will use about 20 GB of space.
<strong>Python:</strong> Python is the main scripting language in CARLA. CARLA supports Python 2.7 and Python 3 on Linux, and Python 3 on Windows.
<strong>Pip:</strong> Some installation methods of the CARLA client library require pip or pip3 (depending on your Python version) version 20.3 or higher. To check your pip version
<strong>Two TCP ports and good internet connection:</strong> 2000 and 2001 by default. Make sure that these ports are not blocked by firewalls or any other applications.
<strong>Other requirements:</strong> CARLA requires some Python dependencies. Install the dependencies according to your operating system: