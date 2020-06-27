import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# set_style()：主题风格
# sns.set_style('whitegrid')
# data = np.random.normal(size=(10,6)) + np.arange(6) / 2
# sns.boxplot(data=data)
# plt.show()
# print(help(np.random.normal))

# sns.set_style('dark')
# data = np.random.normal(size=(10,6)) + np.arange(6) / 2
# sns.boxplot(data=data)
# plt.show()

# print(help(sns.despine))
# print(help(sns.set_context))
# sns.set_style('ticks')
# data = np.random.normal(size=(10,6)) + np.arange(6) / 2
# sns.boxplot(data=data)
# sns.despine()   # 如果不执行这条指令，图标会自动带边框
# plt.show()


# sns.set_style('ticks')
# data = np.random.normal(size=(10,6)) + np.arange(6) / 2
# sns.boxplot(data=data)
# sns.set_context("paper")
# plt.figure(figsize=(10,6))
# plt.show()
#
# sns.set_style('ticks')
# data = np.random.normal(size=(10,6)) + np.arange(6) / 2
# sns.boxplot(data=data)
# sns.set_context("poster")
# plt.figure(figsize=(10,6))
# plt.show()


def sinplot(flip=1):
    x = np.linspace(0, 11, 100)
    for i in range(1, 6):   # 画5条线，所有线都为sin函数
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

# sns.set_context('paper')
# plt.figure(figsize=(10,6))    # figsize=(10,6)：设置图表的大小
# sinplot()
# plt.show()

# sns.set_context('talk')
# plt.figure(figsize=(10,6))
# sinplot()
# plt.show()

# sns.set_context('poster')
# plt.figure(figsize=(10,6))
# sinplot()
# plt.show()

# sns.set_context('paper',font_scale=3)
# plt.figure(figsize=(10,6))
# sinplot()
# plt.show()

sns.set_context('paper',rc={'lines.linewidth':10})
plt.figure(figsize=(10,6))
sinplot()
plt.show()