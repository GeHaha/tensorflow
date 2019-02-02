# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:59:49 2019

@author: 86157
"""

import tensorflow as tf

input1 = tf.placeholder(tf.types.float32)
input2 = tf.placeholder(tf.types.float32)

output = tf.mul(input1,input2)
with  tf.Session() as sess:
    print(sess.run([output],feed_dict= {input:[7.],input2:[2.]}))