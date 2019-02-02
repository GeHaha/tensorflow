# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 18:01:47 2019

@author: 86157
"""
import tensorflow as tf


class SquareTest(tf.test.TestCase):

    def testSquare(self):
        with self.test_session():
            x =  tf.square([2,3])
            self.assertAllEqual(x.eval(),[4,9])

if __name__ == '__mian__':
    tf.test.main()
