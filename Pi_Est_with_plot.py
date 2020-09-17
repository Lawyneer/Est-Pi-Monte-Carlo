# A simple Pyton program to estimate Pi using Monte Carlo Methods
# In this example an estimate of Pi is calculated multiple times
# The various estimates are averaged to arrive at a final estimate

# Import packages and initialize variables
import random            # for the RNG
import matplotlib.pyplot as plt # to generate plots
import time 
import math
random.seed()            # seed RNG with current system time
pis = [ ]                # list to hold various estimates of Pi
total_est = 1           # total estimates of Pi to calculate
rand_x = [ ]
rand_y = [ ]

# Calculate an estimate of Pi multiple time
for k in range(0,total_est):
    # Initialize varable each time Pi is estimated
    circle_points = 0 # Points inside a cirle
    total_points = 0  # Total points
    keep_going = 1    # Termination criteria
    i = 0
    
    # Set up figure for plotting results
    fig = plt.figure()
    ax = fig.add_subplot()
    plt.title('Estimating of Pi using Monte Carlo Methods')
    ax.set_aspect('equal')
    x = [0]
    y_upper = [0]
    y_lower = [0]
    
    # gernate x and y values for circle plot
    for j in range(1, 100000):
        x.append(x[j-1] + 0.00001)
        y_upper.append(math.sqrt(0.25 - (x[j]-0.5)**2) +.5)
        y_lower.append(-math.sqrt(0.25 - (x[j]-0.5)**2) +.5)                
    # end for
    
    plt.plot(x,y_upper, color='black')
    plt.plot(x,y_lower, color='black')
    box_x = [0, 0, 1, 1, 0]
    box_y = [0, 1, 1, 0, 0]
    plt.plot(box_x, box_y, color='black')
    
    i = 0
    while keep_going == 1:  # while loop to estimate pi
        rand_x.append(random.uniform(0, 1)) # x coordinate
        rand_y.append(random.uniform(0, 1)) # y coordiante
        dist = (rand_x[i]-0.5)**2 + (rand_y[i]-0.5)**2   # distance from center of circle
        
        # Determine if point landed inside circle
        if dist <= 0.25:
            circle_points+= 1 # increament points inside circle
        # end if
        
        plt.scatter(rand_x[i], rand_y[i], marker='o', color='red')
        time.sleep(0.1)

        # Increament total points
        total_points+= 1

        # Calculate Pi
        pi = 4* circle_points/total_points
        
        # Test error
        if (pi > 3.140) & (pi < 3.142):
            print(i)
            keep_going = 0 # set termination criteria
            print(keep_going)
        # end if
        
        if (i % 250 == 0):
            print('After', i, 'itterations, the estimate of Pi is:', round(pi,4))
                
        i += 1        
        
    # end while loop

    # Store value of pie
    pis.append(pi)
    
# end for loop

# Calculate final estiamte of Pi
total = sum(pis)                # sum all estimates of Pi
pi = round(total/total_est,5)   # average estimates rounded to 4 decimal places

print("\nThe estimate of Pi is: ", pi,"\n")

