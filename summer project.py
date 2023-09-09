import numpy as np
data=np.loadtxt("Write your txt file's path here")
print(data)
x,y=data[:,0],data[:,1]
import matplotlib.pyplot as plt
#plt.plot(x,y)
def calculate_slope(x1, y1, x2, y2):
    """
    Calculates the slope of a line given two points (x1, y1) and (x2, y2).
    """
    return (y2 - y1) / (x2 - x1)



slopes = []
for i in range(len(x) - 1):
    slope = calculate_slope(x[i], y[i], x[i+1], y[i+1])
    slopes.append(slope)
print('Slope at each data point =',slopes)
print ('Mean slope=',sum(slopes)/len(slopes))

# Plot the line
plt.plot(x, y, 'o-' , label='FM-PM Phase Transition')


# Set the aspect ratio to 'equal' for better visualization
plt.gca().set_aspect('equal')

# Add labels and title
plt.xlabel('log (Temperature)')
plt.ylabel('log (m)')
plt.title('Power law plot')




# Display the legend
plt.legend()

# Show the plot
plt.show()
