from boid import *
from numpy import random
from util import *

dt_middle = 0.01
dt_match = 0.125
clumping_distance = 100
speed_match_distance = 10000

class BoidCommander(object):
  def __init__(self, **kwargs):
    if "number_of_boids" in kwargs:
      self.number_of_boids = kwargs["number_of_boids"]
      self.boids = [
        Boid(random.uniform(*(kwargs["x_pos_bound"])), 
          random.uniform(*(kwargs["y_pos_bound"])),
          random.uniform(*(kwargs["x_velocity_bound"])),
          random.uniform(*(kwargs["y_velocity_bound"])))
        for x in range(self.number_of_boids)
      ]
    elif "init_values" in kwargs:
      xs,ys,xvs,yvs = kwargs["init_values"]
      self.number_of_boids = len(xs)
      self.boids = []
      for i in range(len(xs)):
        self.boids.append(Boid(xs[i],ys[i],xvs[i],yvs[i]))

    else:
      print "please specify \"number_of_boids\" OR \"init_values\""

  def vectorise(self):
    xs = []
    ys = []
    xvs = []
    yvs = []

    for boid in self.boids:
      xs.append(boid.x_position)
      ys.append(boid.y_position)
      xvs.append(boid.x_velocity)
      yvs.append(boid.y_velocity)
    return xs,ys,xvs,yvs


  def fly_towards_middle(self):
    for b1 in self.boids:
      for b2 in self.boids:
        b1.x_velocity += position_update(b2.x_position, b1.x_position, dt_middle, self.number_of_boids)
    
    for b1 in self.boids:
      for b2 in self.boids:
        b1.y_velocity += position_update(b2.y_position, b1.y_position, dt_middle, self.number_of_boids)

  def fly_away_from_nearby_boids(self):
    for b1 in self.boids:
      for b2 in self.boids:
        distance = calculate_distance(b2.x_position, b2.y_position, b1.x_position, b1.y_position)
        if distance < clumping_distance:
            b1.x_velocity+=b1.x_position - b2.x_position
            b1.y_velocity+=b1.y_position - b2.y_position
    
  def try_to_match_speed_with_nearby_birds(self):
    for b1 in self.boids:
      for b2 in self.boids:
        distance = calculate_distance(b2.x_position, b2.y_position, b1.x_position, b1.y_position)
        if distance < speed_match_distance:
            b1.x_velocity+=velocity_update(b2.x_velocity,b1.x_velocity, dt_match,self.number_of_boids)
            b1.y_velocity+=velocity_update(b2.y_velocity,b1.y_velocity, dt_match,self.number_of_boids)

  def move_according_to_velocities(self):
    for boid in self.boids:
      boid.x_position += boid.x_velocity
      boid.y_position += boid.y_velocity

  def update_boids(self):
    self.fly_towards_middle()
    self.fly_away_from_nearby_boids()
    self.try_to_match_speed_with_nearby_birds()
    self.move_according_to_velocities()