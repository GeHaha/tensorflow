# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:55:27 2019

@author: 86157
"""
import tensorflow as tf
import numpy


input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)

intermed = tf.add(input2,input3)
mul = tf.mul(input1,intermed)

with tf.Session() as sess:
    result = sess.run([mul,intermed])
    print(result)
    
    