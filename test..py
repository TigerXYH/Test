import matplotlib.pyplot as plt





x = list(range(1, 5001))
y = [n**3 for n in x]

# plt.plot(x, y, linewidth=5)
plt.scatter(x, y, c=y, cmap=plt.cm.Greens, edgecolors='none', s=10)

# 设置图表名称
plt.title('1~5000', fontsize=24)
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=12)

plt.show()