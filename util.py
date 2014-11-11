def calculate_distance(xa,ya,xb,yb):
  return (xa-xb)**2 + (ya-yb)**2

def position_update(xa,xb,dt,length):
  return (xa-xb)*dt/length

def velocity_update(va,vb,dt,length):
  return (va-vb)*dt/length