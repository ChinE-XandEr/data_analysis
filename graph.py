import matplotlib
matplotlib.use('Agg')  # 设置后端为非交互式
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
import time
import uuid

# 设置seaborn样式
sns.set_style("whitegrid")

def generate_unique_filename():
    """生成唯一的文件名"""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    return f"plot_{timestamp}_{unique_id}.png"

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False     # 用来正常显示负号

# 设置图表大小
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['figure.dpi'] = 100

# 确保plots文件夹存在
if not os.path.exists('plots'):
    os.makedirs('plots')

def set_plot_style():
    """设置每个图表的通用样式"""
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()

def plot_line(input_x, input_y1):
    plt.figure()
    plt.plot(input_x, input_y1, marker='o')
    plt.title('折线图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_bar(input_x, input_y1):
    plt.figure()
    plt.bar(input_x, input_y1)
    plt.title('条形图')
    plt.xlabel('类别')
    plt.ylabel('值')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_histogram(input_x):
    plt.figure()
    plt.hist(input_x, bins=5, edgecolor='black')
    plt.title('柱状图')
    plt.xlabel('值')
    plt.ylabel('频率')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_scatter(input_x, input_y1):
    plt.figure()
    plt.scatter(input_x, input_y1)
    plt.title('散点图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_box(input_x):
    plt.figure()
    plt.boxplot(input_x)
    plt.title('箱线图')
    plt.ylabel('值')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_pie(input_x, input_y1):
    plt.pie(input_y1, labels=input_x, autopct='%1.1f%%')
    plt.title('饼图')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_heatmap(input_x):
    plt.imshow(input_x, cmap='hot', interpolation='nearest')
    plt.title('热力图')
    plt.colorbar()
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_area(input_x, input_y1, input_y2):
    plt.fill_between(input_x, input_y1, label='系列1')
    plt.fill_between(input_x, input_y2, label='系列2')
    plt.title('面积图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.legend()
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_violin(input_x):
    """绘制小提琴图"""
    plt.figure()
    plt.violinplot(input_x)
    plt.title('小提琴图')
    plt.ylabel('值')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_cdf(input_x):
    sorted_data = np.sort(input_x)
    p = 1. * np.arange(len(input_x)) / (len(input_x) - 1)
    plt.plot(sorted_data, p)
    plt.title('累积分布函数图')
    plt.xlabel('值')
    plt.ylabel('累积概率')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()

def plot_scatter_matrix(input_x):
    pd.plotting.scatter_matrix(input_x, alpha=0.2)
    plt.suptitle('散点图矩阵')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()

def plot_3d_scatter(input_x, input_y1, input_y2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(input_x, input_y1, input_y2)
    ax.set_title('三维散点图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_3d_line(input_x, input_y1, input_y2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(input_x, input_y1, input_y2)
    ax.set_title('三维线图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_3d_surface(input_x, input_y1, input_y2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(input_x, input_y1, input_y2, cmap='viridis')
    ax.set_title('三维表面图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_3d_bar(input_x, input_y1, input_y2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    dx = np.ones(len(input_x))
    dy = np.ones(len(input_y1))
    dz = input_y2
    ax.bar3d(input_x, input_y1, input_y2, dx, dy, dz, color='b')
    ax.set_title('三维柱状图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_stem(input_x, input_y1):
    plt.stem(input_x, input_y1)
    plt.title('茎叶图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_step(input_x, input_y1):
    plt.step(input_x, input_y1)
    plt.title('阶梯图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_errorbar(input_x, input_y1, input_y2):
    plt.errorbar(input_x, input_y1, input_y2=input_y2, fmt='o')
    plt.title('误差条图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_fill(input_x, input_y1, input_y2):
    plt.fill_between(input_x, input_y1, input_y2, where=(input_y1 > input_y2), color='blue', alpha=0.3)
    plt.fill_between(input_x, input_y1, input_y2, where=(input_y1 <= input_y2), color='red', alpha=0.3)
    plt.title('填充图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_polar(input_x, input_y1):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(input_x, input_y1)
    ax.set_title('极坐标图')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_contour(input_x, input_y1, input_y2):
    plt.contour(input_x, input_y1, input_y2, levels=10, cmap='viridis')
    plt.title('等高线图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_contourf(input_x, input_y1, input_y2):
    plt.contourf(input_x, input_y1, input_y2, levels=10, cmap='viridis')
    plt.colorbar()
    plt.title('等高线填充图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_density(input_x):
    sns.kdeplot(input_x, shade=True)
    plt.title('密度图')
    plt.xlabel('值')
    plt.ylabel('密度')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_histogram_with_kde(input_x):
    sns.histplot(input_x, kde=True, bins=30)
    plt.title('直方图与核密度估计图')
    plt.xlabel('值')
    plt.ylabel('频率')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_radar(input_x, input_y1):
    angles = np.linspace(0, 2 * np.pi, len(input_x), endpoint=False).tolist()
    input_y1 += input_y1[:1]  # 闭合图形
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, input_y1, color='blue', alpha=0.25)
    ax.set_thetagrids(np.degrees(angles), input_x)
    ax.set_title('雷达图')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()

def plot_waterfall(input_x, input_y1):
    fig, ax = plt.subplots()
    ax.plot(input_x, input_y1, marker='o')
    ax.fill_between(input_x, input_y1, step="pre", alpha=0.4)
    ax.set_title('瀑布图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_scatter3d(x, y, z):
    """绘制三维散点图"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    plt.title('三维散点图')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_line3d(x, y, z):
    """绘制三维线图"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot3D(x, y, z)
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    plt.title('三维线图')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename

def plot_bar3d(x, y, z):
    """绘制三维柱状图"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(x, y, np.zeros_like(z), 0.8, 0.8, z)
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    plt.title('三维柱状图')
    set_plot_style()
    filename = generate_unique_filename()
    plt.savefig(f'plots/{filename}')
    plt.close()
    return filename