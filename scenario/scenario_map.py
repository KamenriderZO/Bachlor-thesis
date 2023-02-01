
class scenario_data():
    map_normal = ['Town01','Town02','Town03','Town05','Town07','Town10HD']
    map_highway = ['Town04','Town06']
    map_all = ['Town01','Town02','Town03','Town04','Town05','Town06','Town07','Town10HD']

    weather_fine = ['Default','ClearNoon','CloudyNoon','WetNoon','WetCloudyNoon','SoftRainNoon','ClearSunset','CloudySunset','WetSunset','WetCloudySunset','SoftRainSunset']
    weather_bad = ['MidRainyNoon','HardRainNoon','MidRainSunset','HardRainSunset']

    traffic_situations = ['smooth','heavy']

    description_1 = "You are starting your car in a town or a city,before you launch the car,you have 1 min to check your car status.Such as seat belt,car doors...then you will drive your car in this town or city."
    description_2 = "You are already driving in the town or the city,no need to care about the seat belt or door anomaly signals.But you have already driven for a long time.Maybe you need to care other anomalies of the car."
    description_3 = "You are travelling on a highway with high speed.It's a long journey and won't stop in a short time."
    description_4 = "You are driving in a bad weather,only bad weathers can be selected.This scenario will focus on how dangerous weather will effect the autonomous driving systems."

    map_info1 = "Map:Town01 is a basic town layout consisting of T junctions."
    map_info2 = "Map:Town02 is a small town."
    map_info3 = "Map:Town03 is the most complex town, with a 5-lane junction, a roundabout, unevenness, a tunnel, and more.."
    map_info4 = "Map:Town04 is an infinite loop with a highway and a small town."
    map_info5 = "Map:Town05 is squared-grid town with cross junctions and a bridge. It has multiple lanes per direction."
    map_info6 = "Map:Town06 is long highways with many highway entrances and exits. It also has a Michigan left."
    map_info7 = "Map:Town07 is a rural environment with narrow roads, barns and hardly any traffic lights."
    map_info10 = "Map:Town10HD is city environment with different environments such as an avenue or promenade, and more realistic textures."

    anomalies_1 = {'door','seatbelt','coolant'}
    anomalies_2 = {'engine','fuel','brake'}

    scenario_1 = {'name': 'scenario_1','map': map_normal,'weather':weather_fine,'description':description_1,'traffic':traffic_situations,'anomalies':anomalies_1}
    scenario_2 = {'name': 'scenario_2','map': map_normal,'weather':weather_fine,'description':description_2,'traffic':traffic_situations,'anomalies':anomalies_2}
    scenario_3 = {'name': 'scenario_3','map': map_highway,'weather':weather_fine,'description':description_3,'traffic':traffic_situations,'anomalies':anomalies_2}
    scenario_4 = {'name': 'scenario_4','map': map_all,'weather':weather_bad,'description':description_4,'traffic':traffic_situations,'anomalies':anomalies_2}
    scenarios = ["None","scenario_1","scenario_2","scenario_3","scenario_4"]