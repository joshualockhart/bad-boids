import yaml
from BoidCommander import BoidCommander
from copy import deepcopy
from numpy import random

x_pos_bound = (-450,50.0)
y_pos_bound = (300.0,600.0)
x_velocity_bound = (0,10.0)
y_velocity_bound = (-20.0,20.0)

num_boids = 50

dt_middle = 0.01
dt_match = 0.125
clumping_distance = 100
speed_match_distance = 10000

xlim=(-500,1500)
ylim=(-500,1500)


b = BoidCommander(number_of_boids=50,
  x_pos_bound=x_pos_bound, 
  y_pos_bound=y_pos_bound, 
  x_velocity_bound=x_velocity_bound,
  y_velocity_bound=y_velocity_bound)

before = deepcopy(b.vectorise())
b.fly_towards_middle()
after = b.vectorise()

fixture={"before":before,"after":after}
fixture_file=open("fly_towards_middle_fixture.yml",'w')
fixture_file.write(yaml.safe_dump(fixture))
fixture_file.close()

quit()

b = BoidCommander(number_of_boids=50,
  x_pos_bound=x_pos_bound, 
  y_pos_bound=y_pos_bound, 
  x_velocity_bound=x_velocity_bound,
  y_velocity_bound=y_velocity_bound)

before = deepcopy(b.vectorise())
b.fly_away_from_nearby_boids()
after = b.vectorise()

fixture={"before":before,"after":after}
fixture_file=open("fly_away_fixture.yml",'w')
fixture_file.write(yaml.safe_dump(fixture))
fixture_file.close()



b = BoidCommander(number_of_boids=50,
  x_pos_bound=x_pos_bound, 
  y_pos_bound=y_pos_bound, 
  x_velocity_bound=x_velocity_bound,
  y_velocity_bound=y_velocity_bound)

before = deepcopy(b.vectorise())
b.try_to_match_speed_with_nearby_birds()
after = b.vectorise()

fixture={"before":before,"after":after}
fixture_file=open("match_speed_fixture.yml",'w')
fixture_file.write(yaml.safe_dump(fixture))
fixture_file.close()



b = BoidCommander(number_of_boids=50,
  x_pos_bound=x_pos_bound, 
  y_pos_bound=y_pos_bound, 
  x_velocity_bound=x_velocity_bound,
  y_velocity_bound=y_velocity_bound)

before = deepcopy(b.vectorise())
b.move_according_to_velocities()
after = b.vectorise()

fixture={"before":before,"after":after}
fixture_file=open("move_according_to_velocities_fixture.yml",'w')
fixture_file.write(yaml.safe_dump(fixture))
fixture_file.close()
