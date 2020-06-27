import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 加载数据，将数据拆分为：训练数据、测试数据
(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()
print(train_image.shape)  # 打印训练数据维度
print(train_label.shape)    # 打印标签的信息

print(train_image[0])   # 打印第一张图片的信息，可看到实际是一个矩阵，取值范围：0-255
plt.imshow(train_image[0])  # plt方法，打印第一张图片
plt.show()

print('打印所有标签：',train_label)
print('打印第一个标签：',train_label[0])

# 数据归一化。图片实际形式为像素矩阵，取值范围为0-255,因此需要归一化，转为0-1的矩阵
train_image = train_image / 255
test_image = test_image / 255

# 搭建模型
model = tf.keras.Sequential()
# 因为输入为2维矩阵，但网络层为1维，因此需将输入矩阵拉直，做扁平化操作
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
# 打印模型
model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['acc'])
model.fit(train_image, train_label, epochs=5)

# 测试
print('测试数据：')
model.evaluate(test_image, test_label)