import numpy as np
import tensorflow as tf
import os
x = np.fft.rfft([0, 1, 0, 0, 0,0,1,2])
y = np.fft.fft([0, 1,  0, 0, 0,0,1])
xx = np.fft.irfft(x)
print(x)
print(xx.real)
print(y)
path = (os.path.abspath)

print(path)

ca = tf.cast(.5, tf.int64)
sess = tf.Session()
print(sess.run(ca))