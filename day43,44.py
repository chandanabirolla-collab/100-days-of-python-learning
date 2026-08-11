import math

print(math.sqrt(16))  # Output: 4.0
from math import pi, sqrt

print(sqrt(25))  # Output: 5.0
# 1. Import built-in modules
import datetime
import math

# Using functions from the imported 'math' module
radius = 5
area = math.pi * (radius**2)

# Using functions from the imported 'datetime' module
current_time = datetime.datetime.now()

# Display results
print(f"Current Date & Time: {current_time}")
print(f"Area of circle with radius {radius}: {area:.2f}")