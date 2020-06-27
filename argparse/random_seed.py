import numpy as np

if __name__ == '__main__':
    i = 0
    while(i<6):
        if(i<3):
            np.random.seed(0)
            # 执行生成随机数前，都令random seed为0，可看到生成的3个随机数全部相同
            print('result',np.random.randn(1, 5))
        else:
            print('result0',np.random.randn(1, 5))
            pass
        i += 1
    i = 0
    print()
    while(i<2):
        print('result1',np.random.randn(1, 5))
        i += 1
    print()
    # 这里生成了2*5的矩阵，发现和循环while(i<8)中的两个1*5矩阵一样，
    # 说明生成多行随机数组时，实际是多个单行矩阵合成的
    print('result3',np.random.randn(2, 5))
    print()
    np.random.seed(0)
    # 可看到后续生成的8个值和之前的结果是一样的，
    # 说明在循环if(i<3)内的random seed对后续的随机值一直都有影响，直到指定新的random seed
    i = 0
    while(i<8):
        print('result',np.random.randn(1, 5))
        i += 1


# import numpy as np
# shuzu = np.array([[1,2,3],[2,2,2]])
# print(shuzu.shape)
# print(shuzu.shape[0])   # 查看行的维度