import tensorflow as tf
import tensorflow.contrib.slim as slim

x1 = tf.to_float(tf.ones(shape = [1, 40000, 1, 2]))
# w = tf.to_float(tf.fill([5, 5, 3, 64], 1))
# print("rank is", tf.rank(x1))
# y1 = tf.nn.conv2d(x1, w, strides=[1, 1, 1, 1], padding='SAME')
y2 = slim.conv2d(x1, 65, [5, 1],stride=3, padding='SAME')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    y2_value,  x1_value = sess.run([ y2, x1])
    print("shapes are",  y2_value.shape)
    # print(y1_value == y2_value)
    # print(y1_value)
    # print(y2_value)
