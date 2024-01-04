#!/usr/bin/env python

"""
Using IMDB data set included with keras
We'll be working with "IMDB dataset", a set of 50,000 highly-polarized reviews 
from the Internet Movie Database. They are split into 25,000 reviews for 
training and 25,000 reviews for testing, each set consisting in 50% negative 
and 50% positive reviews.
"""

import keras
keras.__version__
from keras.datasets import imdb
import numpy as np

# Override np.load() function for keras.datasets.reuters.load_data()
# where np.load() is called 
np_load_old = np.load
np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True)

"""
The argument num_words=10000 means that we will only keep the top 10,000 
most frequently occurring words in the training data. Rare words will be
 discarded. This allows us to work with vector data of manageable size.

The variables train_data and test_data are lists of reviews, each review being 
a list of word indices (encoding a sequence of words). train_labels and 
test_labels are lists of 0s and 1s, where 0 stands for "negative" and 
1 stands for "positive":
"""
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
#[max(sequence) for sequence in train_data]
print("train_data[0]:", train_data[0])
print("shape: ", train_labels.shape)
print ("max: ", max([max(sequence) for sequence in train_data]))

# word_index is a dictionary mapping words to an integer index
word_index = imdb.get_word_index()
# We reverse it, mapping integer indices to words
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
# We decode the review; note that our indices were offset by 3
# because 0, 1 and 2 are reserved indices for "padding", "start of sequence", and "unknown".
decoded_review = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])

print ("decoded review:", decoded_review)

"""
PREPARE DATA
We cannot feed lists of integers into a neural network. We have to turn our 
lists into tensors. 

We could one-hot-encode our lists to turn them into vectors of 0s and 1s.
 Concretely, this would mean for instance turning the sequence [3, 5] into a 
 10,000-dimensional vector that would be all-zeros except for indices 3 and 5, 
 which would be ones. Then we could use as first layer in our network a Dense 
 layer, capable of handling floating point vector data.
We will go with the latter solution. Let's vectorize our data, which we will 
do manually for maximum clarity:
"""
def vectorize_sequences(sequences, dimension=10000):
    # Create an all-zero matrix of shape (len(sequences), dimension)
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.  # set specific indices of results[i] to 1s
    return results

# Our vectorized training data
x_train = vectorize_sequences(train_data)
# Our vectorized test data
x_test = vectorize_sequences(test_data)

print("x_train[0]:", x_train[0])

# Our vectorized labels
y_train = np.asarray(train_labels,dtype=object,).astype('float32')
y_test = np.asarray(test_labels,dtype=object,).astype('float32')

"""
BUILD NETWORK
two intermediate layers with 16 hidden units each, and a third layer which
 will output the scalar prediction regarding the sentiment of the current 
 review. The intermediate layers will use relu as their "activation function", 
 and the final layer will use a sigmoid activation so as to output a 
 probability (a score between 0 and 1, indicating how likely the sample is 
 to have the target "1", i.e. how likely the review is to be positive). A 
 relu (rectified linear unit) is a function meant to zero-out negative values,
 while a sigmoid "squashes" arbitrary values into the [0, 1] interval, thus 
 outputting something that can be interpreted as a probability.
"""
from keras import models
from keras import layers

model = models.Sequential()
model.add(layers.Dense(32, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))


"""
CONFIGURE MODEL
Lastly, we need to pick a loss function and an optimizer. Since we are facing 
a binary classification problem and the output of our network is a probability
 (we end our network with a single-unit layer with a sigmoid activation), is
 it best to use the binary_crossentropy loss. It isn't the only viable choice:
     you could use, for instance, mean_squared_error. But crossentropy is 
     usually the best choice when you are dealing with models that output 
     probabilities. Crossentropy is a quantity from the field of Information 
     Theory, that measures the "distance" between probability distributions, 
     or in our case, between the ground-truth distribution and our predictions.
"""
from keras import optimizers

model.compile(optimizer=optimizers.RMSprop(lr=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])


"""
validataion data
"""
x_val = x_train[:10000]
partial_x_train = x_train[10000:]

y_val = y_train[:10000]
partial_y_train = y_train[10000:]    # 15000


"""
TRAIN
We will now train our model for 4 epochs (4 iterations over all samples in
 the x_train and y_train tensors), in mini-batches of 512 samples. At this
 same time we will monitor loss and accuracy on the 10,000 samples that we
 set apart. This is done by passing the validation data as the validation_data
 argument:
"""
history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=4,
                    batch_size=1024,
                    validation_data=(x_val, y_val))


"""
RESULTS
This object has a member history, which is a dictionary containing data about
 everything that happened during training
It contains 4 entries: one per metric that was being monitored, during 
training and during validation.
"""
results = model.evaluate(partial_x_train, partial_y_train)
print ("train:", results)
results = model.evaluate(x_val, y_val)
print ("validation:", results)
results = model.evaluate(x_test, y_test)
print ("all data", results)

history_dict = history.history
print("history dict.keys():", history_dict.keys())


"""
PLOT LOSS
The dots are the training loss and accuracy, while the solid lines are the 
validation loss and accuracy. Note that your own results may vary slightly 
due to a different random initialization of your network.

As you can see, the training loss decreases with every epoch and the training 
accuracy increases with every epoch. That's what you would expect when running
 gradient descent optimization -- the quantity you are trying to minimize
 should get lower with every iteration. But that isn't the case for the 
 validation loss and accuracy: they seem to peak at the fourth epoch. 
 This is an example of what we were warning against earlier: a model that 
 performs better on the training data isn't necessarily a model that will 
 do better on data it has never seen before. In precise terms, what you are 
 seeing is "overfitting": after the second epoch, we are over-optimizing on 
 the training data, and we ended up learning representations that are specific 
 to the training data and do not generalize to data outside of the training set.

In this case, to prevent overfitting, we could simply stop training after 
three epochs. 
"""
import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

# =============================================================================
# # "bo" is for "blue dot"
# plt.plot(epochs, loss, 'bo', label='Training loss')
# # b is for "solid blue line"
# plt.plot(epochs, val_loss, 'b', label='Validation loss')
# plt.title('Training and validation loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()
# 
# plt.show()
# =============================================================================

"""
plot accuracy
"""
fig, ax = plt.subplots()
ax.plot(epochs, loss, 'bo', label='Training loss')
# b is for "solid blue line"
ax.plot(epochs, val_loss, 'b', label='Validation loss')
ax.set(xlabel='Epochs', ylabel='Loss',
       title='Training and validation loss');
ax.legend()
acc_values = history_dict['accuracy']
val_acc_values = history_dict['val_accuracy']

fig1, ax1 = plt.subplots()
ax1.plot(epochs, acc, 'ro', label='Training acc')
ax1.plot(epochs, val_acc, 'b', label='Validation acc')
ax1.set(xlabel='Epochs', ylabel='Loss',
       title='Training and validation accuracy');
ax1.legend()

plt.show()

"""
predict
"""

testPrediction = model.predict(x_test)
