import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_food():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    food = f.generate()
    # Add noise to the fractal shape to make it look more like food
    noise = np.random.normal(0, 0.05, food.shape)
    food = food + noise
    food = np.clip(food, 0, 1)
    # Apply a food-like color map to the fractal shape
    food = plt.cm.YlOrBr(food)
    # Return the fractal food
    return food

# Generate 10 fractal food images
for i in range(10):
    food = generate_fractal_food()
    plt.imsave("fractal_food_{}.png".format(i), food)
