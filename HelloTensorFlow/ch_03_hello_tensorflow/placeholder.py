import os
import tensorflow as tf
from numpy.random import RandomState

# Eliminate TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# define the size of batch
batch_size = 8


w1 = tf.Variable(tf.random_normal(([2, 3]), stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal(([3, 1]), stddev=1, seed=1))

x = tf.placeholder(tf.float32, shape=(3, 2), name="input")
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

y = tf.sigmoid(y)

cross_entropy = -tf.reduce_mean(y * tf.log(tf.clip_by_value(y, 1e-10, 1.0))
                                +(1-y) * tf.log(tf.clip_by_value(1-y, 1e-10, 1.0)))
learning_rate = 0.001
train_step = tf.train.AdadeltaOptimizer(learning_rate).minimize(cross_entropy)


sess = tf.Session()
init_op = tf.global_variables_initializer()
sess.run(init_op)
print(sess.run(y, feed_dict={x: [[0.7, 0.9], [0.1, 0.4], [0.5, 0.8]]}))