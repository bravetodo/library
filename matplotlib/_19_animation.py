import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

fig, ax = plt.subplots()
x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

# 定义要打印的function
# 设置要打印的function
def animation_function(i):
    line.set_ydata(np.sin(x+i/100))
    return line,

# 设置function的initial状态
def ini_function():
    line.set_ydata(np.sin(x))
    return line,

# 核心：设置ani函数
# fig：要打印的figure
# func=：设置要打印的function
# frames：总共好多帧
# init_func=：设置function的initial状态
# interval：好久更新一帧
# blit=True：意味着只更新figure中变化的点，等于False，则会更新整个figure
ani = animation.FuncAnimation(fig=fig, func=animation_function , frames=100,
                              init_func=ini_function, interval=10, blit=True)

plt.show()