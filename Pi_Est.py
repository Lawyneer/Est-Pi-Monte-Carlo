# A simple Pyton program to estimate Pi using Monte Carlo Methods

# Import packages and initialize variables
import random # for the RNG

circle_points = 0
total_points = 0
keep_going = 1

for k in range(0,10):
    circle_points = 0
    total_points = 0
    keep_going = 1

    while keep_going == 1:
    #for i in range(POINTS**2):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
        dist = rand_x**2 + rand_y**2
        
        if dist <= 1:
            circle_points+= 1
        total_points+= 1

        pi = 4* circle_points/total_points

        if (pi < 3.142) & (pi > 3.140):
            keep_going = 0
            
    print("The estimate of Pi is: ", pi)