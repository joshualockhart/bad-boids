import yaml
from BoidCommander import BoidCommander
from copy import deepcopy
from numpy import random
from config import *

b = BoidCommander(x_pos_bound, 
  y_pos_bound, 
  x_velocity_bound,
  y_velocity_bound,
  dt_match, 
  dt_middle,
  clumping_distance,
  speed_match_distance,
  number_of_boids=number_of_boids
  )

before = deepcopy(b.vectorise())
b.fly_towards_middle()
after = b.vectorise()

fixture={"before":before,"after":after}
fixture_file=open("fly_towards_middle_fixture.yml",'w')
fixture_file.write(yaml.safe_dump(fixture))
fixture_file.close()

b = BoidCommander(x_pos_bound, 
  y_pos_bound, 
  x_velocity_bound,
  y_velocity_bound,
  dt_match, 
  dt_middle,
  clumping_distance,
  speed_match_distance,
  number_of_boids=number_of_boids
  )

before = deepcopy(b.vectorise())
b.fly_away_from_nearby_boids()
after = b.vectorise()

fixture={"before":before,"after":after}
fixture_file=open("fly_away_fixture.yml",'w')
fixture_file.write(yaml.safe_dump(fixture))
fixture_file.close()


b = BoidCommander(x_pos_bound, 
  y_pos_bound, 
  x_velocity_bound,
  y_velocity_bound,
  dt_match, 
  dt_middle,
  clumping_distance,
  speed_match_distance,
  number_of_boids=number_of_boids
  )

before = deepcopy(b.vectorise())
b.try_to_match_speed_with_nearby_birds()
after = b.vectorise()

fixture={"before":before,"after":after}
fixture_file=open("match_speed_fixture.yml",'w')
fixture_file.write(yaml.safe_dump(fixture))
fixture_file.close()



b = BoidCommander(x_pos_bound, 
  y_pos_bound, 
  x_velocity_bound,
  y_velocity_bound,
  dt_match, 
  dt_middle,
  clumping_distance,
  speed_match_distance,
  number_of_boids=number_of_boids
  )

before = deepcopy(b.vectorise())
b.move_according_to_velocities()
after = b.vectorise()

fixture={"before":before,"after":after}
fixture_file=open("move_according_to_velocities_fixture.yml",'w')
fixture_file.write(yaml.safe_dump(fixture))
fixture_file.close()
