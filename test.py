""" import matplotlib.pyplot as plt





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

plt.show() """




n = 1
m = 0
y = 2018
s = 32

# 累交总额
ze = 0
# 领取总额
lqze = 0
# 第8年至65岁间领取均额
je = int(3948 * 0.3)
je2 = je * 1.05


while s <= 105:
    print(str(s) + '岁')
    # 投保概况
    if n <= 15:
        ze += 6000
        print('第' + str(n) + '年累交：' + str(ze))

    # 领取概况
    if n == 6 or n == 7:
        lqze += 6000
        m += 1
        print(str(y) + '年，第' + str(m) + '年领生存金' + str(6000) +
              '。累积领取：' + str(int(lqze)) + '，剩余' + str(int(ze - lqze)))

    elif n > 8 and s < 65:
        lqze += je
        m += 1
        print(str(y) + '年，第' + str(m) + '年领生存金' + str(je) +
              '。累积领取：' + str(int(lqze)) + '，剩余' + str(int(ze - lqze)))

    elif n > 8 and s <= 105:
        lqze += je2
        m += 1
        print(str(y) + '年，第' + str(m) + '年领生存金' + str(int(je2)) +
              '。累积领取：' + str(int(lqze)) + '，剩余' + str(int(ze - lqze)))
        je2 *= 1.05

        if lqze > ze:
            print('多领取：' + str(int(lqze - ze)))

    n += 1
    s += 1
    y += 1
