import matplotlib.pyplot as plt
import numpy as np

n =10
X = np.arange(n)
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
plt.xlim(-.5, n)
plt.ylim(-1.5, 1.5)
plt.xticks(())
plt.yticks(())

plt.bar(X, Y1, facecolor='r', edgecolor='white')   # 柱状图
plt.bar(X, -Y2, facecolor='#9999ff', edgecolor='white')

# 设置text
for x,y in zip(X,Y1): # 这个方法用于loss打印？
    plt.text(x, y+0.05, s='%.2f'%y, ha='center', va='bottom')
for x,y in zip(X,Y2):
    plt.text(x, -y-0.5, s='%.2f'%y, ha='center', va='top')

plt.show()

# # 整体步骤
# # 首先设置柱状图
# plt.bar(X, Y1, facecolor='r', edgecolor='white')   # 柱状图
# plt.bar(X, -Y2, facecolor='#9999ff', edgecolor='white')
#
# # 设置text
# for x,y in zip(X,Y1): # 这个方法用于loss打印？
#     plt.text(x, y+0.05, s='%.2f'%y, ha='center', va='bottom')
# for x,y in zip(X,Y2):
#     plt.text(x, -y-0.5, s='%.2f'%y, ha='center', va='top')

# print(help(plt.bar))