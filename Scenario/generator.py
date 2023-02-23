import glob
import os
import sys

# ==============================================================================
# -- find carla module ---------------------------------------------------------
# ==============================================================================

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
import random
import time

simu_time = 0

actor_list = []
def generate_traffic(situation):
    client = carla.Client('localhost',2000)
    client.set_timeout(30)
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()
    if situation == 'very smooth':
        for i in range (0,len(world.get_map().get_spawn_points())//16):
            bp = random.choice(blueprint_library.filter('vehicle'))
            if bp.has_attribute('color'):
                color = random.choice(bp.get_attribute('color').recommended_values)
                bp.set_attribute('color', color)
            transform = world.get_map().get_spawn_points()[i]
            vehicle = world.try_spawn_actor(bp, transform)
            actor_list.append(vehicle)
            print('created %s' % vehicle.type_id)
            vehicle.set_autopilot(True)
    if situation == 'smooth':
        for i in range (0,len(world.get_map().get_spawn_points())//8):
            bp = random.choice(blueprint_library.filter('vehicle'))
            if bp.has_attribute('color'):
                color = random.choice(bp.get_attribute('color').recommended_values)
                bp.set_attribute('color', color)
            transform = world.get_map().get_spawn_points()[i]
            vehicle = world.try_spawn_actor(bp, transform)
            actor_list.append(vehicle)
            print('created %s' % vehicle.type_id)
            vehicle.set_autopilot(True)
    if situation == 'heavy':
        for i in range (0,len(world.get_map().get_spawn_points())//4):
            bp = random.choice(blueprint_library.filter('vehicle'))
            if bp.has_attribute('color'):
                color = random.choice(bp.get_attribute('color').recommended_values)
                bp.set_attribute('color', color)
            transform = world.get_map().get_spawn_points()[i]
            vehicle = world.try_spawn_actor(bp, transform)
            actor_list.append(vehicle)
            print('created %s' % vehicle.type_id)
            vehicle.set_autopilot(True)
    if situation == 'very heavy':
        for i in range (0,len(world.get_map().get_spawn_points())//2):
            bp = random.choice(blueprint_library.filter('vehicle'))
            if bp.has_attribute('color'):
                color = random.choice(bp.get_attribute('color').recommended_values)
                bp.set_attribute('color', color)
            transform = world.get_map().get_spawn_points()[i]
            vehicle = world.try_spawn_actor(bp, transform)
            actor_list.append(vehicle)
            print('created %s' % vehicle.type_id)
            vehicle.set_autopilot(True)
    time.sleep(5)
# make the log file folder
def mkdir(path):
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

# decide anomalies
def decide_anomaly(s):
    if s['name'] == 'scenario_1':
        return 'door','seatbelt','coolant'
    else:
        return 'engine','fuel','brake'

# decide possibilities
def decide_rate(p):
    if p == "never":
        return 0
    elif p == "low(recommended)":
        return 3
    elif p == "medium":
        return 6
    elif p == "high":
        return 10
    else:
        return simu_time*100

# code frame core to manipulate carla
def generate_scenario(scenario,map,weather,stime,traffic,genrate,fprate,fnrate):
    global simu_time
    mkdir(os.getcwd()+"\\logs")
    files = os.walk(os.getcwd()+"\\logs")
    nr = 1
    while os.path.exists(os.getcwd()+"\\logs\\log_file(username)-"+str(nr)+".txt"):
        nr += 1
    file = open(os.getcwd()+"\\logs\\log_file(username)-"+str(nr)+".txt","a")
    file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" : Initializing carla server...\n")
    print("launching the client...")
    client = carla.Client('localhost',2000)
    client.set_timeout(30)
    world = client.get_world()
    client.load_world(map)
    world.set_weather(eval("carla.WeatherParameters."+weather))
    simu_time = stime*60
    file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" : Parameters decided...\n")
    a1,a2,a3 = decide_anomaly(scenario)
    gen,fp,fn = decide_rate(genrate),decide_rate(fprate),decide_rate(fnrate)
    generate_traffic(traffic)
    file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" : Anomalies set and traffic set...\n")

    file.close()

    cpath = os.getcwd()

    os.system("python "+cpath+"\\scenario\\auto_control.py "
              +" --s="+scenario['name']
              +" --t="+str(simu_time)
              +" --an1="+a1
              +" --an2="+a2
              +" --an3="+a3
              +" --gen="+str(gen)
              +" --fp="+str(fp)
              +" --fn="+str(fn)
              +" --log="+os.getcwd()+"\\logs\\log_file(username)-"+str(nr)+".txt"
              )

    print('destroying actors')
    client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])
    print('done.')
    f = open(os.getcwd()+"\\logs\\log_file(username)-"+str(nr)+".txt","a")
    f.write("Simulation complete.")
    f.close()





    
    
