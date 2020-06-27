import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = x + 1
plt.figure()
plt.plot(x, y, linewidth=30, zorder=1)

# 移动坐标轴位置

    # 首先拿到当前坐标轴
ax = plt.gca()
ax.spines['right'].set_color('none')    # 去掉右边坐标轴
ax.spines['top'].set_color('none')   # 去掉顶部坐标轴
ax.xaxis.set_ticks_position('bottom')   # 设置底部为x坐标轴（可不设置）
ax.yaxis.set_ticks_position('left') # 设置左边为y坐标轴（可不设置）
    # 移动坐标轴
ax.spines['bottom'].set_position(('data', 1))   # 设置1为x坐标轴原点
ax.spines['left'].set_position(('data', 0)) # 设置0为为y坐标轴原点

# 修改坐标轴显示

    # 首先拿到坐标轴
for label in ax.get_xticklabels() + ax.get_yticklabels():
    # 设置宽度
    label.set_fontsize(10)
    # 修改底片
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.8, zorder=2))

plt.show()