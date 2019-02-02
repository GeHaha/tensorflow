# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:00:21 2019

@author: 86157
"""

import tensorflow as tf

#创建一个变量，初始化为标量0

state = tf.Variable(0,name ="counter")

# 创建一个op，其使用是使state增加1

one = tf.constant(1)
new_value = tf.add(state,one)
update = tf.assign(state,new_value)

#启动图后，变量必须先经过初始化(init) op 初始化
#首先必须增加一个初始化op 到图中

init_op = tf.initialize_all_variables()

#启动图，运行op
with tf.Session() as sess:
    #运行init op
    sess.run(init_op)
    print(sess.run(state))
    
    #运行op，更新state ，并打印state
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
        
        









