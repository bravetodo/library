import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np

# 设置数据
(train_image, train_label),(test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()
train_label_onehot = tf.keras.utils.to_categorical(train_label)
test_label_onehot = tf.keras.utils.to_categorical(test_label)

# 搭建模型
model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation=tf.keras.activations.relu))
# 添加一个dropout层
model.add(tf.keras.layers.Dropout(0.5)) # 参数0.5：每次随机丢弃，一半神经元
model.add(tf.keras.layers.Dense(128, activation=tf.keras.activations.relu))
model.add(tf.keras.layers.Dropout(0.5)) # 参数0.5：每次随机丢弃，一半神经元
model.add(tf.keras.layers.Dense(128, activation=tf.keras.activations.relu))
model.add(tf.keras.layers.Dropout(0.5)) # 参数0.5：每次随机丢弃，一半神经元
model.add(tf.keras.layers.Dense(10, activation=tf.keras.activations.softmax))

# 打印模型
model.summary()

# 模型训练
model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=['acc'])
history = model.fit(train_image, train_label_onehot, epochs=10,
                    # validation_data参数用途：添加验证数据，每个epoch训练完后，评估这个model的正确率
                    validation_data=(test_image, test_label_onehot))

# 打印history字典中，有哪些关键词
print(history.history.keys())

plt.plot(history.epoch, history.history.get('loss', 'can not find the key'), label='loss')
plt.plot(history.epoch, history.history.get('val_loss', 'can not find the key'), label='val_loss')
plt.legend()    # 设置标签最佳位置
plt.show()