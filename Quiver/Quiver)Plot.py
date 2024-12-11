# Here we are fabricating functions that shows usage of quiver plot

# imports
import matplotlib.pyplot as plt
import numpy as np


# literals
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)

# Create a meshgrid
X, Y = np.meshgrid(x, y)

# Vector components with more variation
U = -Y
V = X

# Create the quiver plot
plt.quiver(X, Y, U, V)

# defined
def runtheplot(title):
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title(title)
    plt.show()


def quiver_info():
    sp = '~'*100
    print(f"The value for x is -> {x}\n\n\t\tand\n\nThe value for y is -> {y}\n\n")
    print(f"{sp}\n\nThe value for X[meshgrid] is -> {X}\n\n\t\tand\n\nThe value for Y[meshgrid] is -> {Y}\n\n")
    print(f"{sp}\n\nThe value for U[-Y] is -> {U}\n\n\n\nThe value for V[X] is -> {V}\n\n")
    



# Main
quiver_info()