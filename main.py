from config import *
from matplotlib import pyplot as plt
from matplotlib import animation
import BoidCommander

bc = BoidCommander.BoidCommander(x_pos_bound, 
  y_pos_bound, 
  x_velocity_bound,
  y_velocity_bound,
  dt_match, 
  dt_middle,
  clumping_distance,
  speed_match_distance,
  number_of_boids=number_of_boids
  )

figure=plt.figure()
axes=plt.axes(xlim=xlim, ylim=ylim)
bvectorised = bc.vectorise()
scatter=axes.scatter(bvectorised[0],bvectorised[1])

def animate(frame):
   bc.update_boids()
   bvectorised = bc.vectorise()
   scatter.set_offsets(zip(bvectorised[0],bvectorised[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=frames, interval=interval)

if __name__ == "__main__":
    plt.show()


