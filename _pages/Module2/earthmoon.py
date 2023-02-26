from vpython import *
import time

G = 6.67408e-11 # Graviational constant: meters^3/(kg*sec^2)

## Step 1: Setup data for earth/moon
earth = sphere(pos=vector(0,0,0), radius=6e7, color=vector(0,0.5,0.8))
earth_mass = 5.974e24 # kg

moon = sphere(pos=vector(384400000,0,0), radius=1e7, color=vector(0.5,0.5,0.5))
v = vector(0, 0, 1000) # meters/sec

L = label(pos=moon.pos,
    text='', xoffset=20,
    yoffset=50, space=30,
    height=16, border=4,
    font='sans')


## Step 2: Create the animation and apply the laws of physics
last_time = time.time()
total_time = 0
SECONDS_IN_DAY = 24*60*60
while total_time < SECONDS_IN_DAY*60:
    ## Step 2a: Compute the elapsed time since the last frame
    curr_time = time.time()
    dt = (curr_time - last_time)*SECONDS_IN_DAY
    last_time = curr_time
    total_time += dt
    
    ## Step 2b: Apply physics
    arrow = earth.pos - moon.pos
    # Compute the length of the arrow, which is the distance
    # from the earth to the moon
    r = arrow.mag # "magnitude" of the arrow
    # Compute the acceleration
    a = arrow*(G*earth_mass/r**3) # 1/sec^2
    
    # Compute the change in velocity based on the acceleration
    # and the elapsed time using an "Euler step"
    v = v + a*dt
    moon.pos = moon.pos + v*dt
    
    ## Step 3b: Update graphics
    L.pos = moon.pos
    L.text = "{:.3f} Days".format(total_time/SECONDS_IN_DAY)