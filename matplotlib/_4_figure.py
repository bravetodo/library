# 生成一个figure前，就调用一次plt.figure()
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1.100)
y0 = x + 1
y1 = x ** 2

plt.figure(num=0)   # 指定figure编号
plt.plot(x, y0, color='red', linewidth=1.0, linestyle='--') # 指定曲线颜色、宽度、曲线style
plt.plot(x, y1)

plt.figure(num=1,figsize=(2,6)) # 指定figure编号、大小
plt.plot(x, y0, color='red', linewidth=1.0, linestyle='--')
plt.plot(x, y1)

plt.show()