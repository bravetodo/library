import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense())

# 直接通过名称调用
model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['acc'])
# 通过实例化优化器，导入到model.compile中
# 这里损失函数，可不打括号。如果打了括号，就必须要传入参数，
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              loss=tf.keras.losses.categorical_crossentropy(),
              metrics=['acc'])