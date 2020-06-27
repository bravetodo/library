import matplotlib.pyplot as plt
import numpy as np

n = 1000
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
# 设置颜色的值
T = np.arctan2(X, Y)

plt.scatter(X, Y, s=70, c=T, marker='x', cmap=None, alpha=0.5)

plt.xlim(-1,1)
plt.ylim(-1,1)
# 去掉x、y坐标轴
plt.xticks(())
plt.yticks(())
plt.show()


# print(help(plt.scatter))





# plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None,
#         vmin=None, vmax=None, alpha=None, linewidths=None, verts=None,
#         edgecolors=None, hold=None, data=None, **kwargs)