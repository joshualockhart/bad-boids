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