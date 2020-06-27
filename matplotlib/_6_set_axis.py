import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y0 = x + 1
y1 = x ** 2
plt.figure()
plt.plot(x, y0)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# 修改坐标轴长度
plt.xlim(-1, 1) # x坐标轴长度（-1，1）
plt.ylim(-1, 2) # y坐标轴长度（-1，2）

# 修改刻度
# 修改x坐标轴,刻度为：-1， -0.6， -0.2， 0.2， 0.6， 1，
new_ticks = np.linspace(-1, 1, 6)
plt.xticks(new_ticks)
# 修改y坐标轴
plt.yticks([0.00, 0.1, 0.8, 1.6], [r'$really\ low$', r'low', r'good', r'$really\ good\ \alpha$'])

# 修改坐标轴标签
plt.xlabel(r'$this\ is\ input\ \alpha$')    # 加了正则化符号
plt.ylabel('this is output')

# 移动坐标轴位置
# 首先拿到当前坐标轴
ax = plt.gca()
ax.spines['right'].set_color('none')    # 去掉右边坐标轴
ax.spines['top'].set_color('none')   # 去掉顶部坐标轴
# ax.xaxis.set_ticks_position('bottom')   # 设置底部为x坐标轴（可不设置）
# ax.yaxis.set_ticks_position('left') # 设置左边为y坐标轴（可不设置）
# 移动坐标轴
ax.spines['bottom'].set_position(('data', 1))   # 设置1为x坐标轴原点
ax.spines['left'].set_position(('data', 0)) # 设置0为为y坐标轴原点

plt.show()