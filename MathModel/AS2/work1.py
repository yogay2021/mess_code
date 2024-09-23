import matplotlib.pylab as plt
# 人口初始态
x0_0 = [100]
x0_1 = [100]
x0_2 = [100]
x0_3 = [100]
x0_4 = [100]

# 繁殖率初始态
s0_0 = [0.2]
s0_1 = [0.8]
s0_2 = [1.8]
s0_3 = [0.2]
s0_4 = [0.0]

# 存活率t（1-死亡率）
t0 = 0.5
t1 = 0.8
t2 = 0.8
t3 = 0.5

# 动态繁殖率
# 假定资源所能承受的人数上限为30亿
x_max = 30e8
# TODO [ s_n = s_0 * (1 - x / x_max) ]

# 建立人口数列表
x_list = list()
x_list.append(x0_0)
x_list.append(x0_1)
x_list.append(x0_2)
x_list.append(x0_3)
x_list.append(x0_4)

# 建立繁殖率列表
s_list = list()
s_list.append(s0_0)
s_list.append(s0_1)
s_list.append(s0_2)
s_list.append(s0_3)
s_list.append(s0_4)

# 循环时间数
total_time = 200
# print(x_list)
for time in range(total_time):
    xn_0 = (x_list[0][time]*s_list[0][time] +
            x_list[1][time]*s_list[1][time] +
            x_list[2][time]*s_list[2][time] +
            x_list[3][time]*s_list[3][time] +
            x_list[4][time]*s_list[4][time])

    xn_1 = x_list[0][time]*t0
    xn_2 = x_list[1][time]*t1
    xn_3 = x_list[2][time]*t2
    xn_4 = x_list[3][time]*t3

    x_list[0].append(xn_0)
    x_list[1].append(xn_1)
    x_list[2].append(xn_2)
    x_list[3].append(xn_3)
    x_list[4].append(xn_4)

    # 计算总人数
    x_sum = xn_0 + xn_1 + xn_2 + xn_3 + xn_4
    # 更新生育率
    for id_s in range(5):
        s_list[id_s].append(s_list[id_s][0] * (1 - x_sum / x_max))

# 创建一个索引数组，用于X轴
indices = range(len(x_list[0]))
# 绘制数组
# plt.plot(indices, data)
# 绘制第一个数组
plt.plot(indices, x_list[0], label='Data 1', marker='o')  # 使用圆圈标记数据点

# 绘制第二个数组
plt.plot(indices, x_list[1], label='Data 2', marker='s')  # 使用方块标记数据点

# 绘制第三个数组
plt.plot(indices, x_list[2], label='Data 3', marker='^')  # 使用三角标记数据点
plt.plot(indices, x_list[3], label='Data 3', marker='^')
plt.plot(indices, x_list[4], label='Data 3', marker='^')
# 添加标题和标签
plt.title('Array Plot')
plt.xlabel('Index')
plt.ylabel('Value')
# 显示图表
plt.show()