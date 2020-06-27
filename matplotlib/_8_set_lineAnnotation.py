import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = x + 1
plt.figure()
plt.plot(x, y)

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

# 设置曲线标签
# （1，2）点做个annotation
# 首先设置该点
x0 = 1
y0 = x0 + 1
plt.scatter(x0, y0, s=100, color='r')   # 利用散点图标记这个点，点大小设为100，颜色red
plt.plot([x0,x0],[1,y0], 'k--', lw=2)
    # 设置那个点到x坐标轴的投影————实际相当于画一条直线：利用了两点连一条直线原理。
    # 参数：[x0,x0]：两个坐标点x值，[0,y0]：两个坐标点y值，'k--'：颜色black且为虚线，lw=2：显得宽度为2
# 设置annotate参数
plt.annotate(s=r'$this\ is\ x+1=%s$' %y0, xy=(x0,y0), xycoords='data',textcoords='offset points', xytext=(-30,30),
             fontsize=10, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.3'))

# 设置text
plt.text(-1, 1.5, s=r'$this\ is\ a\ \mu\ \sigma_i\ \alpha_t$', fontdict={'size':10, 'color':'b'},withdash=True)

plt.show()