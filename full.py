import matplotlib.pyplot as plt
import numpy as np

##Полный ряд Фурье
pi = np.pi
n = 50


def a_n(k):
    # return 1 / (pi * k) * (-1 * np.sin(2 * pi * k / 3) + (3 / (2 * pi * k)) * (1 - np.cos(2 * pi * k / 3)))
    return 1 / (pi * k) * (-2 * np.sin(4 * pi * k / 3) + (3 / (2 * pi * k)) * (1 - np.cos(4 * pi * k / 3)))


def b_n(k):
    # return 1 / (pi * k) * (3 * np.cos(pi * k) - np.cos(2 * pi * k / 3) + (3 / (2 * pi * k)) * np.sin(2 * pi * k / 3))
    return 1 / (pi * k) * (2 * np.cos(4 * pi * k / 3) - (3 / (2 * pi * k)) * np.sin(4 * pi * k / 3))


def y_2(x):
    if x >= 0 and x < 2:
        return 1 - x
    else:
        return 1


x = np.linspace(0, 3, 100)
y = []
for x_i in x:
    if x_i % 2 == 0 and x_i != 0:
        y_i = 0
    else:
        y_i = 1 / 3
        for i in range(1, n + 1):
            y_i += a_n(i) * np.cos(2 * pi * i * x_i / 3) + b_n(i) * np.sin(2 * pi * i * x_i / 3)
    y.append(y_i)
plt.figure()
plt.yticks([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.xticks([0, 1, 2, 3])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Общий ряд Фурье " + str(n) + "-ого порядка")

plt.plot([0, 1, 2], [1, 0, -1], color='black')
plt.plot([2, 3], [1, 1], color='black')
plt.plot(x, y, color='red', linewidth=1)
plt.show()
