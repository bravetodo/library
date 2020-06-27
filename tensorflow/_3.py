import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

# print(tf.__version__)

# data = pd.read_csv("一个文档路径")
# plt.scatter(data.x, data.y)
# plt.show()
# x = data.x
# y = data.y

x = [1, 2, 3]
y = [4, 5, 6]

# 利用keras搭建一个顺序序列模型（输入一个数据，输出一个数据）
model = tf.keras.Sequential()
    # 参数信息：Dense(输出数据维度，输入数据维度())；
    # 这里输出维度为1，输入为1维元祖数据
model.add(tf.keras.layers.Dense(1, input_shape=(1,)))

# print(model.summary())  # 打印模型

# 编译，不过当后期有自定义的循环后，就不需编译了
model.compile(optimizer='adam', loss='mse') # 训练方法：梯度下降法。损失函数：均方差
history = model.fit(x,y,epochs=1000 )

# 根据训练的模型，输入数据做测试
model.predict(pd.Series([10]))  # pd.Series([10])：输入数据的格式，通过pandas，将数据转为list
