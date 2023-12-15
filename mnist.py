#!/usr/bin/env python

from keras.datasets import mnist
from keras import models
from keras import layers
import numpy as np
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

image_index = 7777 # You may select anything up to 60,000
print(train_labels[image_index]) # The label is 8
# plt.imshow(train_images[image_index], cmap='Greys')
one_image = train_images[image_index]

print('Train Shape', train_images.shape)
print(len(train_labels))
print(train_labels)
print(test_images.shape)
print(len(test_labels))
print(test_labels)

test_images = test_images.reshape((10000, 28*28))
train_images = train_images.reshape((60000, 28*28))

train_images = train_images.astype('float32')/255
test_images = test_images.astype('float32')/255
one_image = one_image.astype('float32')/255

before_categ_test_labels = test_labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network = models.Sequential()
network.add(layers.Dense(512, activation='relu',input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer = 'rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

network.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc)
print(network.summary())

test_probs = network.predict(test_images)
test_preds = np.argmax(test_probs, axis=1)
test_max_probs = np.max(test_probs, axis=1)

stacked_probs = np.column_stack((test_preds, before_categ_test_labels, test_max_probs, test_images))

wrong_predictions = stacked_probs[stacked_probs[:, 0] != stacked_probs[:, 1]]
worst_predictions = wrong_predictions[wrong_predictions[:, 2].argsort()][-9:]
correct_predictions = stacked_probs[stacked_probs[:, 0] == stacked_probs[:, 1]]
best_predictions = correct_predictions[correct_predictions[:, 2].argsort()][-9:]

fig, ax = plt.subplots(3, 3)
fig.suptitle('Worst Predictions')
for i, axi in enumerate(ax.flatten()):
    axi.imshow(worst_predictions[i, 3:].reshape(28, 28), cmap='Greys')
    axi.set_title('Predicted: {}, Actual: {}'.format(int(worst_predictions[i, 0]), int(worst_predictions[i, 1])))

fig1, ax1 = plt.subplots(3, 3)
fig1.suptitle('Best Predictions')
for i, axi in enumerate(ax1.flatten()):
    axi.imshow(best_predictions[i, 3:].reshape(28, 28), cmap='Greys')
    axi.set_title('Predicted: {}, Actual: {}'.format(int(worst_predictions[i, 0]), int(worst_predictions[i, 1])))

plt.show()
