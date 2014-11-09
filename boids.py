"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

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

frames = 50
interval = 50

def init_boids():
  boids_x=[random.uniform(*x_pos_bound) for x in range(num_boids)]
  boids_y=[random.uniform(*y_pos_bound) for x in range(num_boids)]
  boid_x_velocities=[random.uniform(*x_velocity_bound) for x in range(num_boids)]
  boid_y_velocities=[random.uniform(*y_velocity_bound) for x in range(num_boids)]
  return (boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def calculate_distance(xa,ya,xb,yb):
  return (xa-xb)**2 + (ya-yb)**2

def position_update(xa,xb,dt,length):
  return (xa-xb)*dt/length

def velocity_update(va,vb,dt,length):
  return (va-vb)*dt/length

def fly_towards_middle(boids):
  xs,ys,xvs,yvs=boids
  length = len(xs)
  for i,ival in enumerate(xs):
    for j,jval in enumerate(xs):
      xvs[i] += position_update(jval,ival,dt_middle,length)

  for i,ival in enumerate(ys):
    for j,jval in enumerate(ys):
      yvs[i] += position_update(jval,ival,dt_middle,length)

boids = init_boids()

def update_boids(boids):
  xs,ys,xvs,yvs=boids
  
  fly_towards_middle(boids)

  length = len(xs)
  
  for i in range(length):
    for j in range(length):
      distance = calculate_distance(xs[j],ys[j],xs[i],ys[i])
      # Fly away from nearby boids    
      if distance < clumping_distance:
        xvs[i] += (xs[i]-xs[j])
        yvs[i] += (ys[i]-ys[j])
  
  for i in range(length):
    for j in range(length):
      distance = calculate_distance(xs[j],ys[j],xs[i],ys[i])
      # Try to match speed with nearby boids
      if distance < speed_match_distance:
        xvs[i] += velocity_update(xvs[j],xvs[i],dt_match,length)
        yvs[i] += velocity_update(yvs[j],yvs[i],dt_match,length)

  # Move according to velocities
  for i in range(length):
    xs[i] += xvs[i]
    ys[i] += yvs[i]


figure=plt.figure()
axes=plt.axes(xlim=xlim, ylim=ylim)
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=frames, interval=interval)

if __name__ == "__main__":
    plt.show()
