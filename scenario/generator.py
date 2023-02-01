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

anomaly_to_gen = []

simu_time = 0

def decide_time_point(anomalies,simutime):
    for a in anomalies:
        if a['name'] == 'door':
            point = random.randint(10,50)
            a['time_point'] = point
        if a['name'] == 'seatbelt':
            point = random.randint(10,50)
            a['time_point'] = point
        if a['name'] == 'coolant':
            point = random.randint(10,50)
            a['time_point'] = point
        if a['name'] == 'engine':
            point = random.randint(simu_time//5,simu_time*4//5)
            a['time_point'] = point
        if a['name'] == 'fuel':
            point = random.randint(simu_time//5,simu_time*4//5)
            a['time_point'] = point
        if a['name'] == 'brake':
            point = random.randint(simu_time//5,simu_time*4//5)
            a['time_point'] = point

def decide_anomalies(scenario,possibility,fp,fn):
    for a in scenario['anomalies']:
        # anomaly really happened
        number = random.uniform(0,100)
        if number <= possibility :
            false_negative = random.uniform(0,100)
            if false_negative > fn :
                # false negative not happened
                anomaly = {'name':a,'status':'yes','time_point':0}
                anomaly_to_gen.append(anomaly)
            else:
                # false negative happened
                anomaly = {'name':a,'status':'fn','time_point':0}
                anomaly_to_gen.append(anomaly)
        else:
        # anomaly not happened
            false_possitive = random.uniform(0,100)
            if false_possitive > fp :
                # false possitive not happened
                anomaly = {'name':a,'status':'no','time_point':0}
                anomaly_to_gen.append(anomaly)
            else:
                # false possitive happened
                anomaly = {'name':a,'status':'fp','time_point':0}
                anomaly_to_gen.append(anomaly)

actor_list = []
def generate_traffic(situation):
    client = carla.Client('localhost',2000)
    client.set_timeout(30)
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()
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
    else:
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
    time.sleep(5)
# make the log file folder
def mkdir(path):
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

# code frame core to manipulate carla
def generate_scenario(scenario,map,weather,stime,traffic,anomaly,fpositive,fnegative):
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
    decide_anomalies(scenario,anomaly,fpositive,fnegative)
    decide_time_point(anomaly_to_gen,simu_time)
    generate_traffic(traffic)
    file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" : Anomalies set and traffic set...\n")

    file.close()

    cpath = os.getcwd()

    os.system("python "+cpath+"\\scenario\\auto_control.py "
              +" --s="+scenario['name']
              +" --t="+str(simu_time)
              +" --an1="+anomaly_to_gen[0]['name']
              +" --at1="+anomaly_to_gen[0]['status']
              +" --aap1="+str(anomaly_to_gen[0]['time_point'])
              +" --an2="+anomaly_to_gen[1]['name']
              +" --at2="+anomaly_to_gen[1]['status']
              +" --aap2="+str(anomaly_to_gen[1]['time_point'])
              +" --an3="+anomaly_to_gen[2]['name']
              +" --at3="+anomaly_to_gen[2]['status']
              +" --aap3="+str(anomaly_to_gen[2]['time_point'])
              +" --log="+os.getcwd()+"\\logs\\log_file(username)-"+str(nr)+".txt"
              )
    time.sleep(5)
    print('destroying actors')
    client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])
    print('done.')
    f = open(os.getcwd()+"\\logs\\log_file(username)-"+str(nr)+".txt","a")
    f.write("Simulation complete.")
    f.close()





    
    
