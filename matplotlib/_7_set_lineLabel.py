# 标注曲线
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y0 = x + 1
y1 = x ** 2
plt.figure()

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

# 设置曲线标签
plt.plot(x, y0, label='yo')
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='y1')
plt.legend(loc='best')

# 如果要设置重新命名标签(注意：不要忘了逗号！)
# l0, = plt.plot(x, y0, label='Yo')
# l1, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='Y1')
    # 这里通过定义：labels=['line0', 'Y1']，就算之前已经定义过标签，一样会更改
# plt.legend(handles=[l0, l1,], labels=['line0', 'Y1'], loc='lower right')    # 改写了全部标签
# plt.legend(handles=[l0, ], labels=['line0',], loc='lower right')    # 只改写一个标签

plt.show()