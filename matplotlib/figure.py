import matplotlib.pyplot as plt
import numpy as np

# 首先找到一张reward图

# figure图
def figure(x0, y0, x1, y1):
    plt.figure()

    # 设置打印曲线、曲线标签
    plt.plot([0,1], [1,1], label='ps-DDPG', color='r',)
    plt.plot(x1, y1, label='DDPG', color='b')
    plt.legend(loc='best')  # 曲线标签打印位置
    # plt.legend(loc='lower right')

    # 修改x，y坐标轴刻度（x：1——500000迭代次数，y：-100——0reward）
    new_ticks = np.linspace(0, 500000, 6)
    # plt.xticks([],new_ticks)   # 这个要修改，只能将之前的迭代次数换成这个
    plt.yticks([0, 1, 2, 3, 4, 5],['-100', '-80', '-60', '-40', '-20', '0'])

    # 移动y坐标轴：用于能显示x坐标轴左边一点的区域
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('None')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', -0.1))

    # 添加坐标轴标签（x：迭代次数iteration，y：average reward）
    plt.xlabel(s=r'$iteration$')
    plt.ylabel(s=r'$average\ reward$')

    # 添加title
    plt.title(r'$PS-MADDPG\ \ V\ \ DDPG$')

    # 添加text或annotation(先不添加)

    plt.grid()
    plt.tight_layout()
    plt.show()

# test
figure(0,1,1,6)