import matplotlib.pyplot as plt
import numpy as np
import random as rm

N = 500
x = []
y = []
y2 = []
y3 = []
c = []
for item in range(N):
    c.append(float(rm.random()))
for item in range(N):
    x.append(float(rm.random() * 10))
for item in range(N):
    y.append((25 - (x[item] - 5) ** 2) ** (1 / 2) + rm.random() - 0.5)
for item in range(N):
    y2.append(8 - (25 - (x[item] - 5) ** 2) ** (1 / 2) + rm.random() - 0.5)
for item in range(N):
    y3.append((100 - (x[item]) ** 2) ** (1 / 2) + rm.random() - 0.5)
for item in range(N):
    x[item] = x[item] + rm.random() - 0.5
# print(x[0] ** 2 + y[0] ** 2)

plt.figure(figsize=(10, 8))
plt.axis([0, 10, 0, 8])
plt.axis("off")
plt.scatter(x, y, c=c, cmap="jet")
plt.scatter(x, y2, c=c, cmap="jet")
plt.scatter(x, y3, c=c, cmap="jet")
plt.savefig("fig4.png", dpi=300)
plt.show()
