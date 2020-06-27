import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np
import keras
import re

data  = pd.read_csv('./data_code_ppt/data/Tweets.csv')
# print('headline', data.head())
# 文档中，真正会用到的数据，只有两列，因此选择这两列数据
data = data[['airline_sentiment', 'text']]
# 打印评价，有哪些类别
# print('打印评价，有哪些类别：', data.airline_sentiment.unique())
# 打印评价的统计值
# print('打印评价的统计值', data.airline_sentiment.value_counts())
# 这次训练中，只做二分类问题，因此只选择破positive、negative数据，
# 而且因为negative数据太多，因此只选择部分数据训练。
data_p = data[data.airline_sentiment == 'positive']
data_n = data[data.airline_sentiment == 'negative']
data_n = data_n.iloc[:len(data_p)]
data = pd.concat([data_n, data_p]) # 将全部positive、negative数据组合
data = data.sample(len(data)) # 将数据全部打乱

# 数据做预处理：
    # 1、将字符（positive、negative）化成数字，这是为了做二分类
data['review'] = (data.airline_sentiment == 'positive').astype(int) # 将positive、negative数字化
# print('可看到data数据，增加了review这列',data) # 可看到data数据，增加了review这列
print('打印data.review, data.review.values：', data.review, data.review.values)
del data['airline_sentiment']
    # 2、将评论(text栏)中，特殊字符去掉（@等），而且需将文本内容全部转为数字（向量化）
        # 方法：首先需将文本中，特殊字符去掉，将大写字符转为小写字符。
        # 这些完成后，将文本向量化
token = re.compile('[A-Za-z]+[?!,.()]') #
def reg_text(text):
    # 找到文本text中，全部的内容
    new_text = token.findall(text)
    # 将文本text中，全部大写字符，转为小写字符
    new_text = [word.lower() for word in new_text]
    return new_text
data['text'] = data.text.apply(reg_text)
print('打印context的内容：', data['text'])
    # 将文本向量化
        # 首先统计word的个数：通过set()方法，自动去掉重复数据
word_set = set()
for text in data.text:
    for word in text:
        word_set.add(word)
length = len(word_set)
max_word = length + 1 # 这个后期会用到
word_list = list(word_set)
print('打印list中,listen,在list中的位置：', word_list.index('listen,'))
        # 得到了去掉重复数据的文本后，将这个转为字典，这样就能得到一个数字和文本数据的一一对应的字典
word_dict = dict((word, word_list.index(word)+1) for word in word_list)
print('打印word.dict的内容', word_dict)
        # 将文本中的内容，全部换成数字
data_finish = data.text.apply(lambda  x: [word_dict.get(word, 0) for word in x])
# print('data.text的内容：', data.text)
        # 因为文本长度不同，因此需通过填充，将所有文本长度全都调成相同
max_len = max(len(x) for x in data_finish)  # 确定text中，哪个文本最长
print(max_len)
data_finish = keras.preprocessing.sequence.pad_sequences(data_finish.values, maxlen=max_len)
print('打印data_finish：', data_finish.shape)  # 评价已经全部预处理好了

# 模型搭建
model = keras.Sequential()
# Embedding()：将文本映射成，一个密集向量。
# 将data_finish中的文本，全映射为长度10的向量
model.add(keras.layers.Embedding(input_dim=max_word, output_dim=10, input_length=max_len))
model.add(keras.layers.LSTM(64)) # 神经元的个数为64
model.add(keras.layers.Dense(1, activation='sigmoid'))
model.summary()
model.compile(optimizer=keras.optimizers.Adam(),
              loss=keras.losses.binary_crossentropy,
              metrics=['acc'])
# 参数：validation_split：确定将多少训练数据，用于测试数据
history = model.fit(data_finish, data.review, epochs=10, batch_size=128, validation_split=0.2)