# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:06:25 2019

@author: 86157
"""

import tensorflow as tf
from tensorflow.python.framework import ops

#defining varibales
 
weights =tf.Variable(tf.random_normal([2,3],stddev=0.1),
                      name ="weights")
biases = tf.Variable(tf.zeros([3],name = "biases"))
custom_variable = tf.Variable(tf.zeros([3],name="custom"))


#get all the varibales tensors and store them in a list
all_variables_list = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)


#customizd initializer

variable_list_custom = [weights,custom_variable]

#the initializer
init_custom_op = tf.varibales_initializer(var_list = variable_list_custom)


# method_1
# add an op to initialize the a=variables
init_all_op = tf.global_variables_initializer()

# method-2
init_all_op = tf.variables_initializer(var_list = all_variables_list)

# Create another variable with the same value as 'weights'.
weightsNew = tf.Variable(weights.initialized_value(),name = "weightsNew")

init_WeightsNew_op= tf.variables_initializer(var_list = [weightsNew])

# runing the session
with tf.Session() as sess:
    #run the initializer operation
    sess.run(init_all_op)
    sess.run(init_custom_op)
    sess.run(init_WeightsNew_op)
    