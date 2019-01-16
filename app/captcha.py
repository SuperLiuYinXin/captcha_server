# -*- coding: utf-8 -*-
import os
import numpy as np
import tensorflow as tf
from PIL import Image
import logging

log = logging.Logger

data_dir= "/home/liuyinxin/project/captcha_server/data/captcha"


def load_image(path):
    img = Image.open(path).convert("1")
    return np.array(img, dtype=np.ubyte)


# test_dir = "/home/liuyinxin/code/python/tf/data/captcha_test"

labels = os.listdir(data_dir)
print('load strain data set')

image_path_dict = {label: os.listdir("%s/%s" % (data_dir, label)) for label in labels}

X_train = []
y_train = []
for (k, v) in image_path_dict.items():
    y_train += [k] * len(v)
    X_train += [load_image("%s/%s/%s" % (data_dir, k, _)) for _ in v]
#
X_train = np.array(X_train)

# 样本特征   20 * 10

# print('')

trainDataInput = tf.placeholder(shape=[None, 20, 10], dtype=tf.float32)
testDataInput = tf.placeholder(shape=[20, 10], dtype=tf.float32)

x_train = tf.reshape(trainDataInput, [-1, 200])
x_test = tf.reshape(testDataInput, [200])

distance = tf.reduce_sum(tf.abs(tf.add(tf.negative(x_test), x_train)), reduction_indices=1)

# predict = tf.nn.top_k(tf.negative(distance), k)
predict = tf.argmin(distance, axis=0)


# accuracy = 0.  # 准确率


class KnnCaptcha():

    def __init__(self):
        print('captcha_knn_init')
        init = tf.global_variables_initializer()
        sess = tf.Session()
        sess.run(init)
        self.sess = sess
        self.trainDataInput = trainDataInput
        self.y_train = y_train

    def __del__(self):
        self.sess.close()

    def predict(self, tests):
        result = ''
        for test in tests:
            nn_index = self.sess.run(predict, feed_dict={self.trainDataInput: X_train, testDataInput: test})
            result += y_train[nn_index]
        return result


