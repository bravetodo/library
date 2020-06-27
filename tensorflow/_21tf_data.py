# import tensorflow as tf
#
# # 设置一个一维数据
# data = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5, 6,])
#
# print('一维数据类型')
# print(data) # 查看data类型
# for i in data:
#     print('一维数据', i)
# for i in data:
#     print(i.numpy())   # tensor数据转为数字。但不能写成i.np()
#
# # 设置一个二维数据
# data1 = tf.data.Dataset.from_tensor_slices([[1, 2], [3, 4], [5, 6]])
# print('二维数据类型', data1)
# for i in data1:
#     print('二维数据', i)
# for i in data1:
#     print(i.numpy())
#
# # 设置一个字典数据
# data_dict = tf.data.Dataset.from_tensor_slices({'a':[1, 2],
#                                                 'b':[3, 4],
#                                                 'c':[5, 6]})
# print('字典的类型',data_dict)
# for i in data_dict:
#     print('字典的数据',i)
#
# # 选择一部分数据
# print(data.take(1))
# for i in data.take(5):
#     print('选择前5个数字',i)

import tensorflow as tf
# import numpy

data = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5, 6,])
# print(help(data.shuffle))
data0 = data.shuffle(buffer_size=6)  #
for i in data0:
    print('shuffle', i.numpy())
data1 = data0.repeat(count=1)
for i in data1:
    print('repeat' ,i.numpy())
dataset = data1.batch(batch_size=6)
for i in dataset:
    print('batch', i.numpy())

data_ = data.map(tf.square)
data = data.map()
for i in data:
    print(i.numpy())