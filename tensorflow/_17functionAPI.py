import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np
import keras

# print(help(keras.Model()))

# # 数据设置
# (train_image, trian_label),(test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()
# train_image = train_image / 255.0
# test_image = test_image / 255.0
# print(train_image.shape)
#
# # 模型搭建
# input = keras.Input(shape=(28, 28))
#     # keras.layers.Flatten()：相当于一个类，实例化为一个函数。
#     # (input) 为这个函数的参数
# x = keras.layers.Flatten()(input)
# x = keras.layers.Dense(32, activation='relu')(x)
# x = keras.layers.Dropout(0.5)(x)
# x = keras.layers.Dense(64, activation='relu')(x)
# output = keras.layers.Dense(10, activation='softmax')(x)
# model = keras.Model(inputs=input, outputs=output)
# model.summary()
#
# # 模型编译
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
#               metrics=['acc'])
#
# # 模型训练
# history = model.fit(train_image, trian_label, epochs=10,
#           validation_data=(test_image, test_label))


# 数据设置
(train_image, trian_label),(test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()
train_image = train_image / 255.0
test_image = test_image / 255.0
print(train_image.shape)

# 模型搭建
input1 = keras.Input(shape=(28, 28))
input2 = keras.Input(shape=(28, 28))
    # keras.layers.Flatten()：相当于一个类，实例化为一个函数。
    # (input) 为这个函数的参数
x1 = keras.layers.Flatten()(input1)
x2 = keras.layers.Flatten()(input2)
    # Concatenate([x1, x2])：将x1、x2连接到一起
x = keras.layers.concatenate([x1, x2])
x = keras.layers.Dense(32, activation='relu')(x)
output = keras.layers.Dense(10, activation='sigmoid')(x)

model = keras.Model(inputs=[input1, input2], outputs=output)
model.summary()

# 模型编译
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['acc'])

# 模型训练
history = model.fit([train_image[0:10000], test_image], trian_label[0:10000], epochs=1)





