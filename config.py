import yaml
from numpy import random
config = yaml.load(open("config.yml"))

x_pos_bound = config["x_pos_bound"]
y_pos_bound = config["y_pos_bound"]
x_velocity_bound = config["x_velocity_bound"]
y_velocity_bound = config["y_velocity_bound"]
number_of_boids = config["number_of_boids"]
dt_middle = config["dt_middle"]
dt_match = config["dt_match"]
clumping_distance = config["clumping_distance"]
speed_match_distance = config["speed_match_distance"]

xlim = config["xlim"]
ylim = config["ylim"]

frames = config["frames"]
interval = config["interval"]


#B07 Torrington Place 
