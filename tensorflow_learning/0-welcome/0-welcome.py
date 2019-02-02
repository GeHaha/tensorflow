# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import print_function
import tensorflow  as tf
import os


log_dir = os.path.dirname(os.path.abspath(__file__)) + '/logs'

welcome = tf.constant('welcome to tensorslow world')

with tf.Session() as sess:
    writer = tf.summary.FileWriter(os.path.expanduser(log_dir),sess.graph)
    print("output:",sess.run(welcome))
    
writer.close()
sess.close()
