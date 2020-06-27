import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y0 = x + 1
y1 = x ** 2

plt.figure()
plt.plot(x, y0)
plt.plot(x, y1)

# 修改坐标轴长度
plt.xlim((-1, 6)) # x坐标轴长度（-1，1）
plt.ylim((-1, 2)) # y坐标轴长度（-1，2）

# 修改刻度
# 如果x坐标轴,刻度为：-1， -0.6， -0.2， 0.2， 0.6， 1，
# 可用这个方法
new_ticks = np.linspace(-1, 1, 6)
plt.xticks(new_ticks)
# 或者这个方法：plt.xticks(-1, -0.6, -0.2, 0.2, 0.6, 1)
# 修改y坐标轴
plt.yticks([0.00, 0.1, 0.8, 1.6], [r'$really\ low$', r'low', r'good', r'$really\ good\ \alpha$'])   # 修改了字体、添加了书数学符号

# 修改坐标轴标签
plt.xlabel(r'$this\ is\ input\ \alpha$')    # 加了正则化符号，且修改了字体、添加了数学符号
# plt.xlabel('$this\ is\ input\ \\alpha$')    # 不加正则化符号
plt.ylabel('this is output')

plt.show()