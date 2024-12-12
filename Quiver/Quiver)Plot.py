# Here we are fabricating functions that shows usage of quiver plot

# imports
import matplotlib.pyplot as plt
import numpy as np


# literals
plt.rcParams['figure.figsize'] = (13, 9)
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)                                                  # Generates a grid of points
X, Y = np.meshgrid(x, y)

U = -Y                                                                      # Vector field components with more variation
V = X



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
    

def quiver_plot_1():
    plt.quiver(X, Y, U, V)
    runtheplot('Basic Quiver Plot')
    
def quiver_plot_2():
    global U,V
    U += 0.2 * np.random.randn(*X.shape)                                        # We can add some noise to make it more realistic
    V += 0.2 * np.random.randn(*X.shape)
    plt.quiver(X, Y, U, V)
    runtheplot('Quiver Plot With U,V Variation')




# Main
# quiver_info()
quiver_plot_1()
quiver_plot_2()