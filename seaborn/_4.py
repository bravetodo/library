import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 默认颜色
# current_palette = sns.color_palette()
# sns.palplot(current_palette)
# plt.show()

# 增加颜色
# sns.palplot(sns.color_palette('hls',17))
# plt.show()

# data = np.random.normal(size=(10,6)) + np.arange(6) / 2
# sns.boxplot(data=data,palette=sns.palplot(sns.color_palette('hls',10)))
# plt.show()

sns.palplot(sns.color_palette('Paired',10))
plt.show()



# def sinplot(flip=1):
#     x = np.linspace(0, 11, 100)
#     for i in range(1, 6):   # 画5条线，所有线都为sin函数
#         plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

