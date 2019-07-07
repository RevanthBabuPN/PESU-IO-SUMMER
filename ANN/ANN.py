#We are going to use the Pima Indians onset of diabetes dataset
#It describes patient medical record data for Pima Indians and whether they had an onset of diabetes within five years.
#It is a binary classification problem (onset of diabetes as 1 or not as 0). The input variables that describe each patient are numerical.

import tensorflow as tf
import keras # Or import tensorflow.keras as keras
import numpy as np

#Loading the Data
dataset = np.loadtxt('pima-indians-diabetes.data.csv', delimiter=',')
X = dataset[:,0:8]
Y = dataset[:,8]

#Building the NN
#Defining the keras model
model = keras.Sequential ([
    keras.layers.Dense(12, input_dim=8,activation='relu'),
    keras.layers.Dense(8, activation = 'relu'),
    keras.layers.Dense(1, activation = 'sigmoid')
])
#Compiling the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Training the model
model.fit(X, Y, epochs=200)

#Testing the model
test_loss, test_acc = model.evaluate(X, Y)
print("\n\nAccuracy = ",test_acc)
