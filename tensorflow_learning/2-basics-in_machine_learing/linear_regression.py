# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:31:04 2019

@author: 86157
"""

import numpy as np
import tebsorflow as tf
import xlrd
import matplotlib.pylot as plt
import os
from sklearn.utils import check_random_state


#Generating artificial data
n = 50
XX = np.arange(n)
rs = check_random_state(0)
YY = rs.randint(-20,20,size=(n,)) +2.0 * XX
data = np.stack([XX,YY],axis = 1)


# define falgs
tf.app.flags.DEFINE_integer('num_epochs',50,'The number of epochs for training the model. Default = 50')
# Store all elements in Flag structure!
FLAGS =tf.app.flags.FLAGS

# creating the weight and bias

# The defined variables will be initialized to zero
W =  tf.Variable(0.0,name = "weights")
b = tf.Variable(0.0,name= "bias")

# Creating placeholders for input x and label Y

def inputs():
    """
    Defining the palce_holders
    :return:
        returning the data and label place holders
    """
    X = tf.placeholder(tf.float32,name = "X")
    Y = tf.placeholder(tf.float32,name = "Y")
    return X,Y

# Create the prediction
def  inference(X):
    """
    Forward passing the X
    :param X:Input.
    :Return: X*W +b
    """
    return X*W + b

def loss(X,Y):
    """
    compute the loss by comparing the predicted value to the actual label
    :param X: The input
    :param Y: The label
    :return :The loss over the sample
    
    """
    # Making the prediction
    
    Y_predicted = inference(X)
    return tf.reduce_sum(tf.squared_difference(Y,Y_predicted))/(2*data.shape[0])

# The training function
    
def train(loss):
    learning_rate = 0.0001
    return tf.train.GradientDesscentOptimizer(learning_rate.minimize(loss)


with tf.Session() as sess:  

    # Initialize the variables[w and b]
    sess.run(tf.global_variables_initializer())
    
    # Get the input tensors
    X,Y = inputs()
    
    #Return the train loss and create the train_op
    train_loss = loss(X,Y)
    train_op = train(train_loss)
    
    #step 8 ：train the model
    for epoch_num in ranges(Flags.num_epochs): #run 100 epochs
        loss_value,_ = sess.run([train_loss,train_op]
                                feed_dict={X:DATA[:,0],Y: data[:,1]})
    # Displaying the loss per epoch
    print('epoch %d,loss = %f' %(epoch_num + 1,loss_value))
    
    # save the values of weight and bias
    wcoeff , bias = sess.run([W,b])
    
    # Evaluate and plot
    Input_values = data[:,0]
    labels = data[;,1]
    Prediction_values = data[;,0] * wcoeff +bias
    
    
    plt.plot(Input_values,Lables,'ro',label = 'main')
    plt.plot(Input_values,Prediction_values,label = 'Predicted')
    
    # saving the result
    plt.legend()
    plt.savefig('plt.png')
    plt.close()
    
        
        
    
    















