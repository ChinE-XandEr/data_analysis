import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def plot_line(input_x, input_y1):
    plt.plot(input_x, input_y1)
    plt.title('折线图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.show()

def plot_bar(input_x, input_y1):
    plt.bar(input_x, input_y1)
    plt.title('条形图')
    plt.xlabel('类别')
    plt.ylabel('值')
    plt.show()

def plot_histogram(input_x):
    plt.hist(input_x, bins=5, edgecolor='black')
    plt.title('柱状图')
    plt.xlabel('值')
    plt.ylabel('频率')
    plt.show()

def plot_scatter(input_x, input_y1):
    plt.scatter(input_x, input_y1)
    plt.title('散点图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.show()

def plot_box(input_x):
    plt.boxplot(input_x)
    plt.title('箱线图')
    plt.ylabel('值')
    plt.show()

def plot_pie(input_x, input_y1):
    plt.pie(input_y1, labels=input_x, autopct='%1.1f%%')
    plt.title('饼图')
    plt.show()

def plot_heatmap(input_x):
    plt.imshow(input_x, cmap='hot', interpolation='nearest')
    plt.title('热力图')
    plt.colorbar()
    plt.show()

def plot_area(input_x, input_y1, input_y2):
    plt.fill_between(input_x, input_y1, label='系列1')
    plt.fill_between(input_x, input_y2, label='系列2')
    plt.title('面积图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.legend()
    plt.show()

def plot_violin(input_x):
    plt.violinplot(input_x, showmeans=True, showmedians=True)
    plt.title('小提琴图')
    plt.ylabel('值')
    plt.show()

def plot_cdf(input_x):
    sorted_data = np.sort(input_x)
    p = 1. * np.arange(len(input_x)) / (len(input_x) - 1)
    plt.plot(sorted_data, p)
    plt.title('累积分布函数图')
    plt.xlabel('值')
    plt.ylabel('累积概率')
    plt.show()

def plot_scatter_matrix(input_x):
    pd.plotting.scatter_matrix(input_x, alpha=0.2)
    plt.suptitle('散点图矩阵')
    plt.show()

def plot_3d_scatter(input_x, input_y1, input_y2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(input_x, input_y1, input_y2)
    ax.set_title('三维散点图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    plt.show()

def plot_3d_line(input_x, input_y1, input_y2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(input_x, input_y1, input_y2)
    ax.set_title('三维线图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    plt.show()

def plot_3d_surface(input_x, input_y1, input_y2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(input_x, input_y1, input_y2, cmap='viridis')
    ax.set_title('三维表面图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    plt.show()

def plot_3d_bar(input_x, input_y1, input_y2):
    dx = np.ones(len(input_x))
    dy = np.ones(len(input_y1))
    dz = input_y2
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(input_x, input_y1, input_y2, dx, dy, dz, color='b')
    ax.set_title('三维柱状图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    plt.show()

def plot_stem(input_x, input_y1):
    plt.stem(input_x, input_y1)
    plt.title('茎叶图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.show()

def plot_step(input_x, input_y1):
    plt.step(input_x, input_y1)
    plt.title('阶梯图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.show()

def plot_errorbar(input_x, input_y1, input_y2):
    plt.errorbar(input_x, input_y1, input_y2=input_y2, fmt='o')
    plt.title('误差条图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.show()

def plot_fill(input_x, input_y1, input_y2):
    plt.fill_between(input_x, input_y1, input_y2, where=(input_y1 > input_y2), color='blue', alpha=0.3)
    plt.fill_between(input_x, input_y1, input_y2, where=(input_y1 <= input_y2), color='red', alpha=0.3)
    plt.title('填充图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.show()

def plot_polar(input_x, input_y1):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(input_x, input_y1)
    ax.set_title('极坐标图')
    plt.show()

def plot_contour(input_x, input_y1, input_y2):
    plt.contour(input_x, input_y1, input_y2, levels=10, cmap='viridis')
    plt.title('等高线图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.show()

def plot_contourf(input_x, input_y1, input_y2):
    plt.contourf(input_x, input_y1, input_y2, levels=10, cmap='viridis')
    plt.colorbar()
    plt.title('等高线填充图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.show()

def plot_density(input_x):
    sns.kdeplot(input_x, shade=True)
    plt.title('密度图')
    plt.xlabel('值')
    plt.ylabel('密度')
    plt.show()

def plot_histogram_with_kde(input_x):
    sns.histplot(input_x, kde=True, bins=30)
    plt.title('直方图与核密度估计图')
    plt.xlabel('值')
    plt.ylabel('频率')
    plt.show()

def plot_radar(input_x, input_y1):
    angles = np.linspace(0, 2 * np.pi, len(input_x), endpoint=False).tolist()
    input_y1 += input_y1[:1]  # 闭合图形
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, input_y1, color='blue', alpha=0.25)
    ax.set_thetagrids(np.degrees(angles), input_x)
    ax.set_title('雷达图')
    plt.show()

def plot_waterfall(input_x, input_y1):
    fig, ax = plt.subplots()
    ax.plot(input_x, input_y1, marker='o')
    ax.fill_between(input_x, input_y1, step="pre", alpha=0.4)
    ax.set_title('瀑布图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    plt.show()