import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 数据集
# 因为这个数据集，没有head，即全部为数据，因此读取数据时，需写参数header=None
data = pd.read_csv(r'/mnt/hgfs/ShareFolder/chengxu/library/_tensorflow2.0/agriculture1.csv',header=None)
print(data.head())
print('打印标签值统计情况',data.iloc[:,-1].value_counts())   # 打印标签值统计情况

x = data.iloc[:, :-1]
y = data.iloc[:, -1].replace(-1,0)  # 标签中的值，全部为1，-1。为了用逻辑回归方法，因此需要将-1,替换为0,

# 搭建模型
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(4, input_shape=(3,), activation='relu'))
model.add(tf.keras.layers.Dense(4, activation='relu'))   # 这里可不用指定，输出层的维度，tensorflow会自动推断维度
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.summary()

model.compile(optimizer='adam',loss='binary_crossentropy',
              metrics=['acc'])   # metrics:一个统计表格，可统计正确率、损失函数大小等

# 执行训练，将训练获得的数据，放到history中
history = model.fit(x, y, epochs=100)
print('关键词：',history.history.keys())   # 打印history中的关键词

# 打印损失函数，准确率的变化曲线
plt.plot(history.epoch, history.history.get('loss'))    # 参数信息：（训练次数，字典中的loss关键词）
plt.show()
plt.plot(history.epoch, history.history.get('acc')) # 参数信息：（训练次数，字典中的acc关键词）
plt.show()

test = data.iloc[:10, :-1]
model.predict(test)