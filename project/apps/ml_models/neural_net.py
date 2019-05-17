import tensorflow as tf
import tensorflow.keras as layers
import numpy as np
import pandas as pd

def network(batch_size, epochs, alpha, lambda_, h1):
    train = pd.read_csv("../data/adult.data")
    test = pd.read_csv("../data/adult.test")
    both = [train, test]
    data = pd.concat(both, axis=0)
    #data.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'] 
    print(data.columns)
    
    batch_size = batch_size
    epochs = epochs
    alpha = alpha
    lambda_ = lambda_
    h1 = h1
    
    model = tf.keras.Sequential()
    model.add(layers.Dense(784, input_shape=(784,), activation='relu'))
    model.add(layers.Dense(h1, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    
    model.compile(optimizer='sgd',
                 loss = 'categorical_crossentropy',
                 metrics = ['accuracy'])
    
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
    
    eval_train = model.evaluate(x_train, y_train, batch_size=batch_size)
    eval_test = model.evaluate(x_test, y_test, batch_size=batch_size)
    return eval_train, eval_test

network(100, 10, "Preset", 0, 50)
# need to set batch_size to num_examples

print(eval_train)
print(eval_test)

#PREDICT WITH MODEL.PREDICT()