#!/usr/bin/env python

from keras.datasets import mnist
from keras import models

import matplotlib.pyplot as plt
import numpy as np

from scipy import signal
from scipy import misc

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
image_index = 4444  # You may select anything up to 60,000
print(train_labels[image_index])
# =============================================================================
# create subplots 4 rows and 2 columns to display 4 different filters
# =============================================================================
f, axarr = plt.subplots(4, 2)
plt.tight_layout()  # This just makes the titles for the subplots space properly


def show_result(axarr, title):
    global image_index, kernel
    res = signal.convolve2d(train_images[image_index], kernel)
    axarr.set_title(title)
    axarr.imshow(res, cmap="Greys")


# =============================================================================
# Display the first two images before filters
# =============================================================================
axarr[0, 0].imshow(train_images[image_index], cmap="Greys")
axarr[0, 1].imshow(train_images[image_index], cmap="Greys")

# =============================================================================
# # vertical filter bright to dark
# =============================================================================

kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
show_result(axarr[1, 0], "Vertical B->D")

# =============================================================================
# # vertical filter dark to bright
# =============================================================================
kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
show_result(axarr[1, 1], "Vertical D->B")

# =============================================================================
# horizontal filter bright to dark
# =============================================================================
kernel = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
show_result(axarr[2, 0], "Horizontal B->D")

# =============================================================================
# horizontal filter dark to bright
# =============================================================================
kernel = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
show_result(axarr[2, 1], "Horizontal D->B")

# =============================================================================
# # vertical filter sorbel
# =============================================================================
kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
show_result(axarr[3, 0], "Vertical Sobel")

# =============================================================================
# # vertical filter scharr
# =============================================================================
kernel = np.array([[3, 0, -3], [10, 0, -10], [3, 0, -3]])
show_result(axarr[3, 1], "Vertical Scharr")

plt.show()
