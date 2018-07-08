import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 获取随机数字
    rw = RandomWalk()
    rw.fill_walk()

    # 调整尺寸大小
    plt.figure(dpi=128, figsize=(10, 6))

    # 设置点位
    point_numbers = list(range(rw.num_points))    
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s = 1)

    # 设置起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 设置坐标轴隐藏
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break
