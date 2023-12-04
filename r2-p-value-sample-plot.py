import random
import matplotlib.pyplot as plt 


# Define the range for random floating-point values
y_min = 0  # Minimum value
y_max = 100.0  # Maximum value

# Generate 100 random floating-point values within the specified range
random_floats = [random.uniform(y_min, y_max) for _ in range(100)]

# Print the generated random values
for value in random_floats:
    print(value)
    
# Define the range for x values
x_min = 1  # Minimum x value
x_max = 1000   # Maximum x value

# Calculate the step size to evenly divide the range into 100 points
step_size = (x_max - x_min) / 99

# Generate 100 x values within the specified range
x_values = [x_min + i * step_size for i in range(100)]

# Calculate the corresponding y values using y = 2x + 1
y_values = [0.02 * x + 1 for x in x_values]

# Print the generated points
for x, y in zip(x_values, y_values):
    print(f"x: {x}, y: {y}")


# Add random noise to the y values
result = [y + y_noise for y, y_noise in zip(y_values,random_floats)]
# Create a scatter plot for the data points in blue
y_values=result
plt.scatter(x_values, y_values, color='blue', label='Data Points')

# Create a line plot in red
#plt.plot(x_values, y_values, color='red', label='Line Chart')

# Add labels to the chart
plt.xlabel('Weight (kg)', color='black')
plt.ylabel('Fuel Efficiency (mpg)', color='black')

# Add a title to the chart
plt.title('Fuel Efficiency', color='black')

# Add a legend
plt.legend()

# Show the chart
plt.show()