import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(1, 11, 36).reshape(6,6)

plt.imshow(a, interpolation='nearest', cmap='bone', origin='top')
plt.colorbar()  # 打印颜色设置图

plt.xticks(())
plt.yticks(())
plt.show()