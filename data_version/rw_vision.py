from random_walk import RandomWalk
import matplotlib.pyplot as plt

rw1 = RandomWalk(50000)
rw1.fill_walk()
point_numbers = [num for num in range(rw1.num_points)]
# 漫步散点图
plt.scatter(rw1.x_values, rw1.y_values, c=point_numbers,
            cmap=plt.cm.Blues, edgecolor='none', s=10)

# 漫步路线图
# plt.plot(rw1.x_values,rw1.y_values,linewidth=1)

# 突出起止点
plt.scatter(0, 0, c='red', edgecolors='none', s=10)
plt.scatter(rw1.x_values[-1], rw1.y_values[-1],
            c='yellow', edgecolors='none', s=10)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# plt.figure(figsize=(10, 6))
# plt.figure(dpi=128, figsize=(10, 6))
plt.show()
