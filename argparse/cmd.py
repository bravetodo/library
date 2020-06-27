import argparse

# 1. 设置解析器
parser = argparse.ArgumentParser(
    description='My Cmd Line Program',
)

# 2. 定义参数
parser.add_argument('nums',  metavar='num', type=int, nargs='+',
                    help='a num for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the nums (default: find the max)')

# 3. 解析命令行
args = parser.parse_args()

# 4. 业务逻辑
result = args.accumulate(args.nums)
print(result)