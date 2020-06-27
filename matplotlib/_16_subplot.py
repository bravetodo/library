# # 利用subplot2gird
# import matplotlib.pyplot as plt
#
# plt.figure()
# # 打印ax1
# ax1 = plt.subplot2grid((3,3),(0,0), rowspan=1, colspan=3,)
# ax1.plot([1, 6], [1, 6])
# # 注：这些设置和之前的指令不同
# ax1.set_xlabel('x')  # 以前是：plt.xlabel()
# ax1.set_ylabel('y')
# ax1.set_xticks(())
# ax1.set_yticks(())
# ax1.set_title('ax1')    # 以前是：plt.title()
#
# # 打印ax2
# ax1 = plt.subplot2grid((3,3),(1,0), rowspan=1, colspan=2,)
# ax1.plot([1, 6], [1, 6])
#
# # 打印ax3
# ax1 = plt.subplot2grid((3,3),(1,2), rowspan=2, colspan=1,)
# ax1.plot([1, 6], [1, 6])
#
# # 打印ax4
# ax1 = plt.subplot2grid((3,3),(2,0), rowspan=1, colspan=1,)
# ax1.plot([1, 6], [1, 6])
#
# # 打印ax5
# ax1 = plt.subplot2grid((3,3),(2,1), rowspan=1, colspan=1,)
# ax1.plot([1, 6], [1, 6])
#
# # plt.tight_layout()    # 注意加了这个、不加这个的区别
# plt.show()
# # print(help(plt.subplot2grid))


# # 利用gridspec
# import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
#
# plt.figure()
# gs = gridspec.GridSpec(3, 3)    # 生成一个3*3的子图
# ax1 = plt.subplot(gs[0, :]) # 这个子图占一行
# ax2 = plt.subplot(gs[1, :2])
# ax3 = plt.subplot(gs[1:, 2])    # 这个子图占2*1
# ax4 = plt.subplot(gs[2, 0]) # 或者可写为：ax4 = plt.subplot(gs[-1, 0])
# ax5 = plt.subplot(gs[2, 1]) # 或者可写为：ax4 = plt.subplot(gs[-1, -2])
#
# plt.tight_layout()    # 注意加了这个、不加这个的区别
# plt.show()


#
import matplotlib.pyplot as plt

#首先生成好2*2figure
plt.title('a')
figure, ((ax11,ax12),(ax21,ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
# 挨个定义子图((ax11,ax12),(ax21,ax22))
ax11.scatter([0,1],[0,1])

plt.tight_layout()    # 注意加了这个、不加这个的区别
plt.show()
