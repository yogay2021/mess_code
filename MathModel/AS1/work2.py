import matplotlib.pyplot as plt
# 初始车数量
x_0 = 500
y_0 = 1000
# 车辆换城市概率
p_ab = 0.3
p_ba = 0.4
# 还车时间概率
r_1 = 0.7
r_2 = 0.2
r_3 = 0.1
# 循环次数
iters = 10000

x_list = []
y_list = []

x_list.append(x_0)
y_list.append(y_0)

x_1 = r_1*(1-p_ab)*x_0 + r_1*p_ba*y_0
y_1 = r_1*p_ab*x_0 + r_1*(1-p_ba)*y_0
x_list.append(x_1)
y_list.append(y_1)
print("A城车数={}".format(x_1))
print("B城车数={}".format(y_1))

x_2 = r_1*(1-p_ab)*x_1 + r_1*p_ba*y_1 + r_2*(1-p_ab)*x_0 + r_2*p_ba*y_0
y_2 = r_1*p_ab*x_1 + r_1*(1-p_ba)*y_1 + r_2*p_ab*x_0 + r_2*(1-p_ba)*y_0
x_list.append(x_2)
y_list.append(y_2)
print("A城车数={}".format(x_2))
print("B城车数={}".format(y_2))

x_3 = (r_1*(1-p_ab)*x_2 + r_1*p_ba*y_2 +
       r_2*(1-p_ab)*x_1 + r_2*p_ba*y_1 +
       r_3*(1-p_ab)*x_0 + r_3*p_ba*y_0)
y_3 = (r_1*p_ab*x_2 + r_1*(1-p_ba)*y_2 +
       r_2*p_ab*x_1 + r_2*(1-p_ba)*y_1 +
       r_3*p_ab*x_0 + r_3*(1-p_ba)*y_0)
x_list.append(x_3)
y_list.append(y_3)
print("A城车数={}".format(x_3))
print("B城车数={}".format(y_3))
for id_n in range(4,iters):
    x_new = (r_1*(1-p_ab)*x_list[id_n-1] + r_1*p_ba*y_list[id_n-1] +
             r_2*(1-p_ab)*x_list[id_n-2] + r_2*p_ba*y_list[id_n-2] +
             r_3*(1-p_ab)*x_list[id_n-3] + r_3*p_ba*y_list[id_n-3])

    y_new = (r_1*p_ab*x_list[id_n-1] + r_1*(1-p_ba)*y_list[id_n-1] +
             r_2*p_ab*x_list[id_n-2] + r_2*(1-p_ba)*y_list[id_n-2] +
             r_3*p_ab*x_list[id_n-3] + r_3*(1-p_ba)*y_list[id_n-3])
    x_list.append(x_new)
    y_list.append(y_new)

    print("A城车数={}".format(x_new))
    print("B城车数={}".format(y_new))



