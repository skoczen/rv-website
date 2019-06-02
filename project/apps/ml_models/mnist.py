#import tensorflow as tf
#from tensorflow.keras import layers
#import numpy as np
#import pandas as pd
#import os

#def create_model():
#    model = tf.keras.models.Sequential([
#        tf.keras.layers.Flatten(input_shape=(28, 28)),
#        tf.keras.layers.Dense(128, activation='relu'),
#        tf.keras.layers.Dropout(0.2),
#        tf.keras.layers.Dense(10, activation='softmax')
#      ])
    
#    model.compile(optimizer = 'adam',
#                 loss = 'sparse_categorical_crossentropy',
#                 metrics=['accuracy'])
#    return model

def guess_number(pixel_array):
    
#    model = create_model()
#    model.load_weights('checkpoint/cp.ckpt')
    
#    return model.predict(pixel_array)
    return 0
