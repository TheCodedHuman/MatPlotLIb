# Here we are fabricating a program to learn about imshow() within matplotlib.pyplot

# imports
import matplotlib.pyplot as plt
import numpy as np


# literals
# plt.rcParams['figure.figsize'] = (12, 8)
pth = r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Imager\Example_Image_for_ImShow.jpg"
x = plt.imread(pth)

# Defined
def image_1():

    lst = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]]
    pixel_info = np.array(lst)                          # demonstrating the pixels we can see and increase
    print(f'\n{pixel_info}\n')

    plt.imshow(pixel_info)
    plt.title('Basic Image Show Functioning')
    plt.show()


def image_2():

    sz = 500
    pixL = np.array([[1, 0]*sz, [0, 1]*sz]*sz)
    print(f"\n{pixL}\n")

    plt.imshow(pixL,cmap='grey')                      # Try cmap='cool'
    plt.title('imshow With Added Functionalities')
    plt.show()


def image_3():
    
    print(x)                                          # Image pixel information
    plt.figure(figsize=(5, 5))
    plt.imshow(x)
    plt.show()


def image_4():                                          # Stretching the image [equal, auto]
    
    plt.imshow(x, aspect='auto')
    plt.show()


def image_5():

    plt.imshow(x, 
               cmap='grey',                 # cmap='grey' wont work simply here like an attribute here because cmap don't work on rgba images
               alpha=0.75, 
               origin='lower')              # starts plotting data from bottom up
    plt.show()


def image_6():                              
                                            # the image I used was a rgb image, that's why [pixels_x, pixels_y, layer_no.] came like this
    print(x.shape)


def image_7():
    
    plt.imshow(x[:,:,1], cmap= 'grey', aspect='equal',  origin='upper', resample=False)
    plt.show()


def image_8():
    pass

# Main
# image_1()
# image_2()
# image_3()
# image_4()
# image_5()
# image_6()
# image_7()






'''
@} Basic Syntax
plt.imshow(X, cmap=None, norm=None, aspect=None, interpolation=None,
           alpha=None, vmin=None, vmax=None, origin=None, extent=None,
           shape=None, filternorm=1, filterrad=4.0, resample=None, url=None, **kwargs)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@} Some Key attributes and parameters of imshow()

X: The image data. This can be a 2D (for greyscale) or 3D (for RGB or RGBA) array.

cmap: Colormap to use for mapping the data values to colors (only relevant for single-channel data).
Example: cmap='gray' for greyscale.

norm: Normalize the data values to the range [0, 1] for the colormap.
Example: norm=plt.Normalize(vmin=0, vmax=255).

aspect: Aspect ratio of the image.
Example: aspect='auto' (default is 'equal').

interpolation: How the image should be interpolated.
Examples: interpolation='nearest', interpolation='bicubic'.

alpha: The alpha blending value, between 0 (transparent) and 1 (opaque).
Example: alpha=0.5.

vmin, vmax: Used to scale the data values to the color map.
Example: vmin=0, vmax=255.

origin: Place the [0, 0] index of the array at the 'upper' or 'lower' corner of the axes.
Example: origin='lower'.

extent: The bounding box in data coordinates that the image will fill.
Example: extent=[-2, 2, -2, 2].
'''


# # Extra information to know
# text annotate legend
# fill between
