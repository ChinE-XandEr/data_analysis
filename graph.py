import matplotlib
matplotlib.use('Agg')  # 设置后端为非交互式
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
import time

# 设置seaborn样式
sns.set_style("whitegrid")

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False     # 用来正常显示负号

# 设置图表大小和其他参数
plt.rcParams.update({
    'figure.figsize': [10, 6],
    'figure.dpi': 100,
    'savefig.dpi': 100,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1
})

# 确保static文件夹存在
if not os.path.exists('static'):
    os.makedirs('static')

def save_plot(plot_type='plot'):
    """
    保存图表的通用函数
    Args:
        plot_type: 图表类型，用于生成文件名
    Returns:
        生成的文件名
    """
    try:
        # 设置全局样式
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout(pad=2.0)  # 增加边距
        
        # 生成唯一的文件名
        timestamp = int(time.time() * 1000)  # 毫秒级时间戳
        filename = f'plot_{plot_type}_{timestamp}.png'
        filepath = os.path.join('static', filename)
        
        # 保存图表
        plt.savefig(filepath, 
                   bbox_inches='tight',  # 自动调整边界
                   pad_inches=0.5,      # 增加边距
                   dpi=100,             # 设置分辨率
                   facecolor='white',   # 设置背景色
                   edgecolor='none',    # 移除边框
                   transparent=False)    # 不使用透明背景
        
        # 清理旧文件（保留最近的20个文件）
        clean_old_plots()
        
        return filename
    except Exception as e:
        print(f"保存图表时出错: {e}")
        raise
    finally:
        plt.close('all')  # 确保关闭所有图表

def clean_old_plots(keep_last_n=20):
    """
    清理旧的图表文件，只保留最近的n个文件
    """
    try:
        static_dir = 'static'
        # 获取所有plot_开头的png文件
        plots = sorted(
            [f for f in os.listdir(static_dir) if f.startswith('plot_') and f.endswith('.png')],
            key=lambda x: os.path.getmtime(os.path.join(static_dir, x))
        )
        
        # 删除旧文件
        for old_plot in plots[:-keep_last_n]:
            try:
                os.remove(os.path.join(static_dir, old_plot))
            except Exception as e:
                print(f"删除旧图表文件时出错: {e}")
    except Exception as e:
        print(f"清理旧图表文件时出错: {e}")

def set_plot_style():
    """设置每个图表的通用样式"""
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()

def plot_line(x, y):
    """绘制折线图"""
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.title('折线图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    return save_plot('line')

def plot_bar(x, y):
    """绘制条形图"""
    plt.figure(figsize=(10, 6))
    if isinstance(x[0], (int, float)):
        plt.bar(range(len(x)), y)
        plt.xticks(range(len(x)), x)
    else:
        plt.bar(x, y)
    plt.title('条形图')
    plt.xlabel('类别')
    plt.ylabel('值')
    return save_plot('bar')

def plot_histogram(x):
    """绘制直方图"""
    plt.figure(figsize=(10, 6))
    # 使用Sturges公式计算最佳bin数量
    bins = int(np.log2(len(x)) + 1)
    plt.hist(x, bins=bins, edgecolor='black', alpha=0.7, density=True)
    # 添加核密度估计曲线
    kde = sns.kdeplot(data=x, color='red', linewidth=2)
    plt.title('直方图与密度曲线')
    plt.xlabel('值')
    plt.ylabel('频率')
    return save_plot('histogram')

def plot_scatter(x, y):
    """绘制散点图"""
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    plt.title('散点图')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    return save_plot('scatter')

def plot_box(x):
    """绘制箱线图"""
    plt.figure(figsize=(10, 6))
    plt.boxplot(x, patch_artist=True)
    plt.title('箱线图')
    plt.ylabel('值')
    return save_plot('box')

def plot_violin(x):
    """绘制小提琴图"""
    plt.figure(figsize=(10, 6))
    plt.violinplot(x)
    plt.title('小提琴图')
    plt.ylabel('值')
    return save_plot('violin')

def plot_scatter3d(x, y, z):
    """绘制三维散点图"""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 绘制数据点
    scatter = ax.scatter(x, y, z, c=z, cmap='viridis', 
                        marker='o', s=50, alpha=0.6)
    
    # 添加颜色条
    plt.colorbar(scatter)
    
    # 设置轴标签和标题
    ax.set_xlabel('X轴', labelpad=10)
    ax.set_ylabel('Y轴', labelpad=10)
    ax.set_zlabel('Z轴', labelpad=10)
    ax.set_title('三维散点图', pad=20)
    
    # 调整视角
    ax.view_init(elev=20, azim=45)
    
    # 保证三个坐标轴的比例一致
    ax.set_box_aspect([1, 1, 1])
    
    # 调整布局并保存
    plt.tight_layout()
    return save_plot('scatter3d')

def plot_line3d(x, y, z):
    """绘制三维线图"""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 绘制3D线条
    line = ax.plot3D(x, y, z, linewidth=2, alpha=0.8)
    
    # 添加散点以标记关键点
    ax.scatter(x, y, z, c='red', marker='o', s=30, alpha=0.6)
    
    # 设置轴标签和标题
    ax.set_xlabel('X轴', labelpad=10)
    ax.set_ylabel('Y轴', labelpad=10)
    ax.set_zlabel('Z轴', labelpad=10)
    ax.set_title('三维线图', pad=20)
    
    # 调整视角
    ax.view_init(elev=20, azim=45)
    
    # 保证三个坐标轴的比例一致
    ax.set_box_aspect([1, 1, 1])
    
    # 调整布局并保存
    plt.tight_layout()
    return save_plot('line3d')

def plot_bar3d(x, y, z):
    """绘制三维柱状图"""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 设置柱子的宽度
    dx = np.ones_like(x) * 0.5
    dy = np.ones_like(y) * 0.5
    
    # 绘制3D柱状图
    bars = ax.bar3d(x, y, np.zeros_like(z), dx, dy, z,
                    color='skyblue', alpha=0.8, shade=True)
    
    # 设置轴标签和标题
    ax.set_xlabel('X轴', labelpad=10)
    ax.set_ylabel('Y轴', labelpad=10)
    ax.set_zlabel('Z轴', labelpad=10)
    ax.set_title('三维柱状图', pad=20)
    
    # 调整视角
    ax.view_init(elev=20, azim=45)
    
    # 保证三个坐标轴的比例一致
    ax.set_box_aspect([1, 1, 1])
    
    # 调整布局并保存
    plt.tight_layout()
    return save_plot('bar3d')