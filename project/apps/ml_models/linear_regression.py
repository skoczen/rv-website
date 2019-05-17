import tensorflow as tf
import tensorflow.keras as layers
import numpy as np
import pandas as pd

def linear(alpha, epochs):
    #IMPORTING AND FORMATTING DATA HERE(convert to tensor)
    data = pd.read_csv('../data/housing.csv')
    data = data.iloc[:, [2,3,4,5,6,7,8,9,10,11,12,13,14,15,19]]
    #data = data.reset_index(drop=True)
    
    train = data.iloc[0:12967]
    train_x = train[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
       'waterfront', 'view', 'condition', 'grade', 'sqft_above',
       'sqft_basement', 'yr_built', 'yr_renovated', 'sqft_living15']].values
    train_y = train['price'].values
    #np.reshape(train_y, (12967, 1))
    #print(train_x.shape)
    
    val = data.iloc[12968:17290]
    val_x = val[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
       'waterfront', 'view', 'condition', 'grade', 'sqft_above',
       'sqft_basement', 'yr_built', 'yr_renovated', 'sqft_living15']].values
    val_y = val['price'].values
    
    test = data.iloc[17291:21613]
    test_x = test[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
       'waterfront', 'view', 'condition', 'grade', 'sqft_above',
       'sqft_basement', 'yr_built', 'yr_renovated', 'sqft_living15']].values
    test_y = test['price'].values
    
    alpha = alpha
    theta = tf.zeros(14)
    epochs = epochs
    
    h = np.matmul(train_x, theta)
    cost = tf.reduce_mean(tf.losses.mean_squared_error(train_y, h))
    train = tf.train.GradientDescentOptimizer(alpha).minimize(cost)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(epochs):
            sess.run(train)
    return cost, theta
      
linear(0.001, 10)

print(cost)
eval = tf.losses.sigmoid_cross_entropy(test_y, tf.matmul(test_y*theta))
print(eval)

#PREDICT WITH X_TEST*THETA