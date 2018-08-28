import tensorflow as tf
from tensorflow.contrib import slim
import numpy as np

x = tf.to_float(tf.ones(shape = [1, 40000, 1, 2]))
y1 = slim.conv2d(x, 64,  [3, 3], scope = 'sf/conv1_1', stride = 1)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sf_value = sess.run([y1])
    sf_value_ = sess.run([y1, x])

    print(sf_value.shape)


