import yaml
import boids
from copy import deepcopy

# fly towards middle test
before=deepcopy(boids.boids)
boids.fly_towards_middle(boids.boids)
after=boids.boids
fixture={"before":before,"after":after}
fixture_file=open("fly_towards_middle_fixture.yml",'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()

before=deepcopy(boids.boids)
boids.fly_away_from_nearby_boids(boids.boids)
after=boids.boids
fixture={"before":before,"after":after}
fixture_file=open("fly_away_fixture.yml",'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()

before=deepcopy(boids.boids)
boids.try_to_match_speed_with_nearby_birds(boids.boids)
after=boids.boids
fixture={"before":before,"after":after}
fixture_file=open("match_speed_fixture.yml",'w')
fixture_file.write(yaml.dump(fixture)) 
fixture_file.close()

before=deepcopy(boids.boids)
boids.move_according_to_velocities(boids.boids)
after=boids.boids
fixture={"before":before,"after":after}
fixture_file=open("move_according_to_velocities_fixture.yml",'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()  
