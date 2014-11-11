from boids import *
from nose.tools import assert_almost_equal, assert_equal
import os
import yaml

def test_bad_boids_regression():
  regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
  boid_data=regression_data["before"]
  update_boids(boid_data)
  for after,before in zip(regression_data["after"],boid_data):
    for after_value,before_value in zip(after,before): 
      assert_almost_equal(after_value,before_value,delta=0.01)

def test_distance_calculation():
  data = yaml.load(open(os.path.join(os.path.dirname(__file__),'distance_fixture.yml')))
  
  calculated_distances = []
  for point_list in data["points"]:
    print "---"
    print point_list
    
    xa = point_list[0][0]
    ya = point_list[0][1]

    xb = point_list[1][0]
    yb = point_list[1][1]

    calculated_distances.append(calculate_distance(xa,ya,xb,yb))
  
  distances = data["distances"]
  for i,dist in enumerate(calculated_distances):
    assert_almost_equal(dist, distances[i], delta=0.01)

def test_fly_towards_middle():
  regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fly_towards_middle_fixture.yml')))
  boid_data=regression_data["before"]
  fly_towards_middle(boid_data)
  for after,before in zip(regression_data["after"],boid_data):
    for after_value,before_value in zip(after,before): 
      assert_almost_equal(after_value,before_value,delta=0.01)

def test_position_update():
  assert_almost_equal(position_update(300,200,0.01,50),0.02)

def test_velocity_update():
  assert_almost_equal(velocity_update(300,10,0.01,50), 0.058)
  

def test_fly_away_from_nearby_boids():
  regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fly_away_fixture.yml')))
  boid_data=regression_data["before"]
  fly_away_from_nearby_boids(boid_data)
  for after,before in zip(regression_data["after"],boid_data):
    for after_value,before_value in zip(after,before): 
      assert_almost_equal(after_value,before_value,delta=0.01)

def test_try_to_match_speed_with_nearby_birds():
  regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'match_speed_fixture.yml')))
  boid_data=regression_data["before"]
  try_to_match_speed_with_nearby_birds(boid_data)
  for after,before in zip(regression_data["after"],boid_data):
    for after_value,before_value in zip(after,before): 
      assert_almost_equal(after_value,before_value,delta=0.01)

def test_move_according_to_velocities():
  regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'move_according_to_velocities_fixture.yml')))
  boid_data=regression_data["before"]
  move_according_to_velocities(boid_data)
  for after,before in zip(regression_data["after"],boid_data):
    for after_value,before_value in zip(after,before): 
      assert_almost_equal(after_value,before_value,delta=0.01)
