# A simple Pyton program to estimate Pi using Monte Carlo Methods
# In this example an estimate of Pi is calculated multiple times
# The various estimates are averaged to arrive at a final estimate

# Import packages and initialize variables
import random # for the RNG
random.seed()  # seed RNG with current system time
pis = [ ]     # list to hold various estimates of Pi
total_est = 10 # total estimates of Pi to calculate

# Calculate an estimate of Pi multiple time
for k in range(0,total_est):
    # Initialize varable each time Pi is estimated
    circle_points = 0 # Points inside a cirle
    total_points = 0  # Total points
    keep_going = 1    # Termination criteria

    while keep_going == 1:  # while loop to estimate pi
        rand_x = random.uniform(-1, 1) # x coordinate
        rand_y = random.uniform(-1, 1) # y coordiante
        dist = rand_x**2 + rand_y**2   # distance from center of circle
        
        # Determine if point landed inside circle
        if dist <= 1:
            circle_points+= 1 # increament points inside circle
        # end if

        # Increament total points
        total_points+= 1

        # Calculate Pi
        pi = 4* circle_points/total_points
        
        # Test error
        if (pi < 3.142) & (pi > 3.140):
            keep_going = 0 # set termination criteria
        # end if
    # end while loop

    # Store value of pie
    pis.append(pi)
    
# end for loop

# Calculate final estiamte of Pi
total = sum(pis)                # sum all estimates of Pi
pi = round(total/total_est,4)   # average estimates rounded to 4 decimal places

print("\nThe estimate of Pi is: ", pi,"\n")

