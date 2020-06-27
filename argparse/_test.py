# import tensorflow as tf
#
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.Dense(10, activation='softmax'))
#
# model.summary()

# import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
# import keras
import datetime
import os

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.mnist.load_data()
train_image = np.expand_dims(train_image, -1)
test_image = np.expand_dims(test_image, -1)
print(train_image.shape, test_image.shape)  # 可看到train_image为四维。（图片张数，长， 宽，RGB通道）
train_image = tf.cast(train_image/255, tf.float32) # 首先将数据归一化，然后转为32位数据
test_image = tf.cast(test_image/255, tf.float32)
train_label = tf.cast(train_label, tf.int64)
test_label = tf.cast(test_label, tf.int64)
dataset = tf.data.Dataset.from_tensor_slices((train_image, train_label))
test_dataset = tf.data.Dataset.from_tensor_slices((test_image, test_label))
print(dataset, test_dataset)
dataset = dataset.repeat().shuffle(60000).batch(128)
test_dataset = test_dataset.repeat().batch(128)

# 模型搭建
model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3),
                              input_shape=train_image.shape[1:], # 因为train_image第一维，为图片的张数
                              activation='relu'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.MaxPool2D())
model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=(3,3),
                                 activation='relu'))
# GlobalAveragePooling2D()：每层数据求平均值，求完后，将这些平均值，组成一维数据。有点像flatten函数，将矩阵拉直。
model.add(tf.keras.layers.GlobalAveragePooling2D())
model.add(tf.keras.layers.Dense(10, activation='softmax'))
model.summary()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['acc'])

# 设施tensorboard
# 设置存放log文件的位置，这里给log文件，添加了时间
log = os.path.join('log', datetime.datetime.now().strftime('%y%m%d-%h%m%s'))
# 通过callbacks函数，调用Tensorboard。
# 参数：log_dir：文件的名字。histogram_freq：多久保存一次数据，这里设置为，每个epoch就保存一次数据
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log, histogram_freq=1)
# 设置好了log文件的位置，需要在训练程序中，通过callbacks这个参数，调用定义好的tesorboard
history = model.fit(dataset, epochs=10,
                    steps_per_epoch=60000//128, # 当传入一个无线数据集时，需指定这个参数，告诉系统，迭代多少个step，算一个epoch
                    validation_data=test_dataset,
                    validation_steps=10000//128,
                    callbacks=[tensorboard_callback])
print(history.history.keys())
