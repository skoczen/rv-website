import tensorflow as tf
import tensorflow.keras as layers
import numpy as np
import pandas as pd

def normal():
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
    #print(train_y.shape)
    
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
    
    theta = tf.zeros(14, dtype='float64')

    tf.convert_to_tensor(train_x); tf.math.l2_normalize(train_x)
    tf.convert_to_tensor(train_y); tf.math.l2_normalize(train_y)
    tf.convert_to_tensor(theta);
    tf.convert_to_tensor(test_x); tf.math.l2_normalize(test_x)
    tf.convert_to_tensor(test_y); tf.math.l2_normalize(test_y)
    
    theta = tf.reshape(theta, [-1,1])
    test_y = tf.reshape(test_y, [-1,1])
    train_y = tf.reshape(train_y, [-1,1])
    
    cost = tf.losses.sigmoid_cross_entropy(train_y, tf.matmul(train_x, theta))
    eval = tf.losses.sigmoid_cross_entropy(test_y, tf.matmul(test_x, theta))
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print(sess.run(cost))
        print(sess.run(eval))
    
    theta = tf.matmul(tf.linalg.inv(tf.matmul(tf.transpose(train_x), train_x)), tf.matmul(tf.transpose(train_x), train_y))
    
    theta = tf.reshape(theta, [-1,1])
    
    cost = tf.losses.sigmoid_cross_entropy(train_y, tf.matmul(train_x, theta))
    eval = tf.losses.sigmoid_cross_entropy(test_y, tf.matmul(test_x, theta))
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print(sess.run(cost))
        print(sess.run(eval))
    #return cost, eval, theta

normal()

#print(cost)
#eval = tf.losses.sigmoid_cross_entropy(test_y, np.matmul(test_x, theta))
#print(eval)

#PREDICT WITH X_TEST*THETA