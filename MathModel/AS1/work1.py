from matplotlib import pyplot as plt
import numpy as np

x = [9.6, 18.3, 29.0, 47.2, 71.1, 119.1, 174.6]
y = [8.7, 10.7, 18.2, 23.9, 48.0, 55.5, 82.7]
x2 = np.arange(0,200,1)
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
plt.scatter(x, y)
plt.plot(x2, 0.5*x2)
plt.xlabel("Pn")
plt.ylabel("DeitaP")
plt.title('DeltaP-Pn')

#使用show展示图像
plt.show()
