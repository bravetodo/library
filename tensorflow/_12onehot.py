import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np

(train_image, train_label),(test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()
print(train_label[1])
train_label_onehot = tf.keras.utils.to_categorical(train_label)
print(train_label_onehot[1])
print(test_label[2])
test_label_onehot = tf.keras.utils.to_categorical(test_label)
print(test_label_onehot[2])

# 搭建模型
model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# 打印模型
model.summary()

# 训练模型
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=['acc'])
model.fit(train_image, train_label_onehot, epochs=5)

# 评估模型
evaluate = model.evaluate(test_image,test_label_onehot)
print('评估',evaluate)

# 用该模型预测
predict = model.predict(test_image)
print(predict.shape)
print(predict[0])
print(np.argmax(predict[0]))