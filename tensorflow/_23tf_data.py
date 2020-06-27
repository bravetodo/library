import tensorflow as tf
# import matplotlib.pyplot as plt

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.mnist.load_data()

# train_image = train_image/255
# test_image = test_image/255
# print('trian_image_shape维度：', train_image.shape)
# dataset_train_image = tf.data.Dataset.from_tensor_slices(train_image)
# dataset_train_label = tf.data.Dataset.from_tensor_slices(train_label)
# print('dataset_train_image信息：', dataset_train_image)
# dataset_train = tf.data.Dataset.zip((dataset_train_image, dataset_train_label))
# print('dataset_train信息：', dataset_train)

# 上述注释方法，有点复杂，这样的方法更好
train_image = tf.cast(train_image/255, tf.float32)
train_label = tf.cast(train_label, tf.int32)
dataset_train = tf.data.Dataset.from_tensor_slices((train_image, train_label))
print('dataset_train信息：', dataset_train)
test_image = tf.cast(test_image/255, tf.float32)
test_label = tf.cast(test_label, tf.int32)
dataset_test = tf.data.Dataset.from_tensor_slices((test_image, test_label))
print('dataset_test信息：', dataset_test)

dataset_train = dataset_train.shuffle(10000).repeat().batch(128)
dataset_test = dataset_test.batch(128)

# 模型搭建
model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
model.summary()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['acc'])
# 设置tensorboard
import os
import datetime
log_dir = os.path.join('log', datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S'))
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir='log', histogram_freq=1)
# 当传入一个无限数据集时，需指定这个参数，告诉系统，迭代多少个step，算一个epoch
steps_per_epoch=train_image.shape[0] // 128
# 如果测试数据为，无限数据集时，需告诉系统，迭代多少个step
validation_steps = test_image.shape[0] // 128

history = model.fit(dataset_train, epochs=10,
                    steps_per_epoch=steps_per_epoch,
                    validation_data=dataset_test,
                    validation_steps=validation_steps,
                    callbacks=[tensorboard_callback])
print(history.history.keys())

# plt.plot(history.epoch, history.history.get('loss'))
# plt.show()
# plt.plot(history.epoch, history.history.get('acc'))
# plt.show()