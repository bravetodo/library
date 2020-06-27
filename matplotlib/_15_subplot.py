import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2, 1, 1)    # 将图分为2行1列，这个子图占第一行
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 4)    # 将图分为2行3列，注意这个子图占的位置
plt.plot([0, 1], [0, 2])

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 3])

plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 4])

plt.show()