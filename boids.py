import random
from numpy import array


class Boid(object):
    def __init__(self,x,y,xv,yv,owner):
        self.position=array([x,y])
        self.velocity=array([xv,yv])
        self.owner=owner

    def specific_interaction(self, other, seperation, seperation_sq): pass

    def interaction(self, other):
        delta_v=array([0.0,0.0])
        separation=other.position-self.position
        separation_sq=separation.dot(separation)
        return delta_v+self.specific_interaction(other, separation, separation_sq)

class Eagle(Boid):
    def specific_interaction(self, other, separation, separation_sq):
        return separation*self.owner.eagle_hunt_strength

class Starling(Boid):
    def specific_interaction(self, other, separation, separation_sq):
        # Fly towards the middle
        delta_v=separation*self.owner.flock_attraction
            
        # Fly away from nearby boids
        if separation_sq < self.owner.avoidance_radius**2:
            delta_v-=separation

        # Try to match speed with nearby boids
        if separation_sq < self.owner.formation_flying_radius**2:
            delta_v+=(other.velocity-self.velocity)*self.owner.speed_matching_strength

        return delta_v



# Deliberately terrible code for teaching purposes
class Boids(object):
    def __init__(self,
           flock_attraction,avoidance_radius,
            formation_flying_radius,speed_matching_strength,
            eagle_avoidance_radius=100, eagle_fear=5000, eagle_hunt_strength=0.00005):
        self.flock_attraction=flock_attraction
        self.avoidance_radius=avoidance_radius
        self.formation_flying_radius=formation_flying_radius
        self.speed_matching_strength=speed_matching_strength
        self.eagle_avoidance_radius=eagle_avoidance_radius
        self.eagle_fear=eagle_fear
        self.eagle_hunt_strength=eagle_hunt_strength


    def initialise_random(self,count):
        """
        self.boids=[Boid(random.uniform(-450,50.0),
                random.uniform(300.0,600.0),
                random.uniform(0,10.0),
                random.uniform(-20.0,20.0),self) for i in range(count)]
        """
        self.boids=[Starling(random.uniform(-450,50.0),
                random.uniform(300.0,600.0),
                random.uniform(0,10.0),
                random.uniform(-20.0,20.0),self) for i in range(count)]


    def add_eagle(self,x,y,xv,yv):
        #self.boids.append(Boid(x,y,xv,yv,self,species="Eagle"))
        self.boids.append(Eagle(x,y,xv,yv,self))

    def initialise_from_data(self,data):
        #self.boids=[Boid(x,y,xv,yv,self) for x,y,xv,yv in zip(*data)]
        self.boids=[Starling(x,y,xv,yv,self) for x,y,xv,yv in zip(*data)]

    def update(self):
        for me in self.boids:
            delta_v=array([0.0,0.0])
            for him in self.boids:
                delta_v+=me.interaction(him)
            # Accelerate as stated
            me.velocity+=delta_v
            # Move according to velocities
            me.position+=me.velocity


