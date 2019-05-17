import tensorflow as tf
import tensorflow.keras as layers
import numpy as np
import pandas as pd

def logistic(alpha, epochs):
    IMPORTING AND FORMATTING DATA HERE(convert to tensor)
    
    alpha = alpha
    theta = tf.zeros(num_features)
    epochs = epochs
    
    h = tf.sigmoid(np.matmul(x_train, data))
    cost = tf.losses.sigmoid_cross_entropy(y_train, h)
    train = tf.reduce_mean(tf.train.GradientDescentOptimizer(alpha).minimize(cost))
    
    with tf.Session() as sess: 
        sess.run(tf.global_variables_initializer())
        for i in range(epochs):
            sess.run(train)
    return cost, theta

logistic(0.001, 10)

print(cost)
eval = tf.losses.sigmoid_cross_entropy(y_test, tf.sigmoid(tf.matmul(x_test*theta)))
print(eval)
#PREDICT WITH SIGMOID(X_TEST*THETA)