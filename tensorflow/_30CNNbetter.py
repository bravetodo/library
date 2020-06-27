import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
import keras

# 数据导入
(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()
train_image = np.expand_dims(train_image, -1)
test_image = np.expand_dims(test_image, -1)
print(train_image.shape, test_image.shape)  # 可看到train_image为四维。（图片张数，长， 宽，RGB通道）

# 模型搭建
model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=(3,3),
                              input_shape=train_image.shape[1:], # 因为train_image第一维，为图片的张数
                              activation='relu'))
model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=(3,3),
                              activation='relu'))
model.add(tf.keras.layers.MaxPool2D())
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=(3,3),
                                 activation='relu'))
model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=(3,3),
                                 activation='relu'))
model.add(tf.keras.layers.MaxPool2D())
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=(3,3),
                                 activation='relu'))
model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=(2,2),
                                 activation='relu',))
model.add(tf.keras.layers.Dropout(0.5))
# GlobalAveragePooling2D()：每层数据求平均值，求完后，将这些平均值，组成一维数据。有点flatten函数，将矩阵拉直。
model.add(tf.keras.layers.GlobalAveragePooling2D())
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
model.summary()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['acc'])
history = model.fit(train_image, train_label, epochs=10,
          validation_data=(test_image, test_label))
print(history.history.keys())

# 打印结果
plt.plot(history.epoch, history.history.get('loss'))
plt.plot(history.epoch, history.history.get('val_loss'))
plt.show()
plt.plot(history.epoch, history.history.get('acc'))
plt.plot(history.epoch, history.history.get('val_acc'))
plt.show()