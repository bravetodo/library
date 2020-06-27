import numpy as np
# shuzu = np.array([[1,2,3],[2,2,2]], dtype=np.int)
# print(shuzu)
# print(shuzu.ndim)   # 查看数组的维度
# print(shuzu.nbytes)
# print(shuzu.shape)  # 查看数组的行列大小
# print(shuzu.size)   # 查看矩阵内有多少个元素


# a = [1,2,3] # 定义一个列表
# print(a)
# b = np.array([1,2,3], dtype=np.int64) # 定义为64位整数类型的矩阵
# print(b)
# print(b.dtype)
# c = np.zeros((3,2),dtype=np.int)    # 定义一个3*3大小的整数类型0矩阵
# print(c)
# d = np.ones((3,2))  # 定义3*2大小的1矩阵
# print(d)
# e = np.empty((3*1)) # 定义3*1大小的空矩阵，但这个矩阵不是真为空，是生成接近于0的矩阵
# print(e)
# f = np.arange(1,10,2)  # 生成范围为（1，10）有序矩阵，且步长为2
# print(f)
# g = np.arange(6).reshape((3,2))   # 生成一个3*2的有序矩阵
# print(g)
# g = [i for i in range(10) if i%2!=0]    # 定义一个列表
# print(g)
# h = np.linspace(1,10,6) # 线段（1，10）内，自动生成6个随机数，而且包含1，10，数字类型为浮点型
# print(h)
# i = np.linspace(1,10,6).reshape((3,2))  # 随机生成一个3*2的矩阵
# print(i)
# k = np.random.random((2,2)) # 生成一个（0，1）范围内的2*2矩阵
# print(k)
# a = np.arange(6,0,-1).reshape((3,2))  # 生成一个范围为（6，0），步长为-1的矩阵，相当于生成一个倒序矩阵
# print('倒序矩阵',a)

# a = np.arange(4)
# b = np.array([5,6,7,8])
# c = np.array([5,6,7,8,9])
# # 矩阵内元素运算
# print(a,'\n',b)
# print(a - b)    # 矩阵内的元素逐个进行相减
# print(a + b)
# print(a * b)
# # 矩阵乘法
# a = np.arange(4).reshape((2,2))
# b = np.array([5,6,7,8]).reshape((2,2))
# d_dot = np.dot(a,b)
# print('矩阵乘法：',d_dot)
# print(np.dot(a,b.T))    # a乘以b的转置矩阵
# print(a.dot(b)) # 矩阵a*b
# print(a.dot(b.T))   # a乘以b的转置矩阵
#
# 常用三角函数
# print(10*np.sin(a)) # 对矩阵内元素求sin值，然后乘以10，
# print(np.tan(a))

#　判断矩阵内元素值大小
# print(a < 3)    # 判断矩阵a内哪些元素小于3，然后返回一个布尔值
# print(a == 3)
# print(a < b)
# 求和、最大值、最小值、求平均值
# a = np.array([[1,2],[3,4]])
# print(a)
# print('求和',np.sum(a))
# print(np.sum(a,axis=0)) # 对a矩阵列数求和
# print(np.sum(a,axis=1)) # 对a矩阵行数求和
# print('求最小值',np.min(a))
# print(np.min(a,axis=0)) # 找到一列中的最大值
# print(np.max(a))
# print(np.average(a))    # 求a矩阵平均值
# print(np.mean(a))   # 求a矩阵平均值
# print(np.mean(a,axis=1,dtype=float))    # 计算行平均值，且值转为float
# print(a.mean())
# print(a.mean(axis=0,dtype=int)) # 计算列平均值，且值转为int

# # 求最值索引
# a = np.arange(1,10).reshape((3,3))
# print(a)
# print(np.argmin(a)) # 求列表中最小值的位置
# print(a.argmin())   ## 求列表中最小值的位置
# print(np.argmin(a,axis=1))  # 找到一行中最小值的位置
# print(np.argmax(a))
# # 求中位数
# b = np.array([[1,2],[5,6]])
# print('中位数',np.median(b))
# print(b.mean())
# # 对矩阵内元素求逐个累加和
# a = np.array([[1,2],[3,4]])
# print('矩阵内元素累加和：',np.cumsum(a))
# # 对矩阵内元素求逐个累差
# b = np.array([[3,2,1],[5,6,6],[3,2,0]])
# print('矩阵内元素求逐个累差:',np.diff(b))
# # 找到矩阵内的非零元素
# print('非零元素：',np.nonzero(b))
# # 输出结果为：(array([0, 0, 0, 1, 1, 1, 2, 2], dtype=int64), array([0, 1, 2, 0, 1, 2, 0, 1], dtype=int64))
# # 上述结果表达含义：哪些位置元素非零，
# # 就输出这些元素的位置，第一个为行位置，第二个为列位置，
# # 比如位置0行1的元素为2为非零。但位置2行2列的元素为0，所以不输出这个结果
#
# # 对矩阵排序，和列表排序差不多
# b = np.array([[1,2,3],[5,6,6],[3,2,0]])
# print('排序',np.sort(b))
# # 矩阵转置
# b = np.array([[1,2,3],[5,6,6],[3,2,0]])
# print('转置',np.transpose(b))
# print('转置',b.T)
#
#
# # 矩阵clip，和ppo算法的clip一样
# b = np.array([[1,2,3],[5,6,6],[3,2,0]])
# # 将矩阵内小于3的值，变为3。大于5的值，变为5。大于3且小于5的不变
# print(np.clip(b,3,5))
#
#
# # 数组的索引
# array = np.array([[1,2,3],[5,6,6],[3,2,0]])
# print(array[0][1])
# print(array[0,1])
# print(array[0,:])   # 输出0行位置的所有元素
# print(array[1,0:2]) # 输出1行位置中，0到1列的元素
#
# for row in array:   # 整行整行的输出数据
#     print('行',row)
# for column in array.T:  # 整列整列的输出数据，
#         # 转置array的原因：因为python中不支持整列输出，所以通过转置，间接输出整行数据
#     print('列',column)
# print(array.flatten())  # 将多行矩阵拉直，转为一行矩阵
# for iterate in array.flat:  # 一个一个输出矩阵中的元素
#     print(iterate,end=' ')
# print()
#
#
# array = np.random.randn(10) * .5
# print(array)


# array的合并、分割