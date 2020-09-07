# A simple Pyton program to estimate Pi using Monte Carlo Methods

# Import packages and initialize variables
import random # for the RNG

for k in range(0,10):
    # Initialize variables for each loop
    circle_points = 0 # Points inside a circle
    total_points = 0  # Total points
    keep_going = 1    # Termination criteria

    while keep_going == 1:  # while loop to estimate pi
        rand_x = random.uniform(-1, 1) # x coordinate
        rand_y = random.uniform(-1, 1) # y coordinate
        dist = rand_x**2 + rand_y**2   # distance from center of circle
        
        # Determine if point landed inside circle
        if dist <= 1:
            circle_points+= 1
        # end if
        
        # Increament total points
        total_points+= 1
        
        # Calculate Pi
        pi = 4* circle_points/total_points
        
        # Test for error
        if (pi < 3.142) & (pi > 3.140):
            keep_going = 0 # Set termination criteria when error small
    
    # Print estimate of Pi
    print("The estimate of Pi is: ", pi)
    
