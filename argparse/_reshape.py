import numpy as np

a = np.random.random((2,2)) # 生成一个随机矩阵
print('a',a)
b = a.reshape(-1,1) # 将矩阵转为1列矩阵
print('b',b)

i = 6
for i in range(1, 11):
    print(i)
    print(i+1)