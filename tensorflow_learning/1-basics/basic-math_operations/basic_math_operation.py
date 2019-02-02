# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 18:09:19 2019

@author: 86157
"""
from __future__ import print_function
import tensorflow as tf
import os

tf.app.flags.DEFINE_string(
        'log_dir',os.path.dirname(os.path.abspath(__file__)) + '/logs',
        'Directory where event logs are written to.')

# store all elements in FLAG structure！
FLAGS = tf.app.flags.FLAGS

if not os.path.isabs(os.path.expanduser(FLAGS.log_dir)):
    raise ValueError('You must assign absolute path for --log_dir')
    
# Defining some constabt values
    
a = tf.constant(5.0,name ='a')
b = tf.constant(10.0,name = 'b')

#some basic operations
x= tf.add(a,b,name = "add")
y = tf.add(a,b,name = "divide")


#run the session
with tf.Session() as sess:
    
    writer = tf.summary.FileWriter(os.path.expenduser(FLAGS.log_dir),sess.graph)
    print('a=',sess.run(a))
    print('b=',sess.run(b))
    print("a+b=",sess.run(x))
    print("a/b=",sess.run(y))
    
#closeing the write
write.close()
sess.close()
