import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = np.linspace(-1,1,100)
y = x ** 2

# 首先设置大图在整个figure中所占比例:
    # left, bottom：子图在整个figure中的位置
    # width, height：子图在整个figure中的比例
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8

# 设置子图ax1
    # 设置子图ax1大小
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('ax1')

# 设置子图ax1
    # 设置子图ax2大小
ax3 = fig.add_axes([0.15, 0.15, 0.2, 0.2])
ax3.plot(x, x, 'b')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_title('ax3')

# 设置子图ax0
plt.axes([0.6, 0.5, 0.2, 0.2])
plt.plot(y, y, 'y')
plt.xlabel('x')
plt.ylabel('y')
plt.title('ax0')

plt.show()