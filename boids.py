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
clumping = 100
speed_match = 10000

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

boids = init_boids()

def update_boids(boids):
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	length = len(xs)
	for i,ival in enumerate(xs):
		for j,jval in enumerate(xs):
			xvs[i] += (jval-ival)*dt_middle/length

	for i,ival in enumerate(ys):
		for j,jval in enumerate(ys):
			yvs[i] += (jval-ival)*dt_middle/length

	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < clumping:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < speed_match:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*dt_match/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*dt_match/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]


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
