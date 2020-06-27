import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print('tensorflow version:{}' .format(tf.__version__))

data = pd.read_csv(r'/mnt/hgfs/ShareFolder/chengxu/library/_tensorflow2.0/agriculture.csv')
print(data.head())  # 打印数据特征列
plt.scatter(data.a, data.d)
plt.show()

# iloc：pandas函数。data.iloc[:,[0]] 提取所有行中，[0]列的数据

x = data.iloc[:, 0:-1]  # 提取所有行中，[0:-1]列的所有数据
y = data.iloc[:, -1]    # 提取最后一列数据

# 搭建一个三层模型。输入层：输入维度为3,输出维度为10。隐藏层：输入维度为10，输出维度10，激活函数为relu。
# 输出层：输入维度为10,输出维度为1
# 这里可这样写，亦可通过model_add的方法，添加网络层
model = tf.keras.Sequential([tf.keras.layers.Dense(10, input_shape=(3,),activation='relu'),
                            tf.keras.layers.Dense(1)])

# 打印模型
model.summary()

# 设置优化器，损失函数
model.compile(optimizer='adam', loss='mse')
# 训练模型
model.fit(x, y, epochs=1000)

# 通过测试数据，测试下模型的效果d
test = data.iloc[:10, 0:-1] # 设置测试数据
test_result = data.iloc[:10, -1]    # 设置的测试数据，真正对应的标签值
print('test')
model.predict(test)
print('result',test_result)  #  打印标签值，和预测值做对比