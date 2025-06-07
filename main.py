from flask import Flask, request, jsonify, redirect, url_for, send_from_directory
import threading
import time
import os
from flask import send_file
from flask_cors import CORS
import numpy as np
from graph import *

app = Flask(__name__)
CORS(app)

# 确保plots文件夹存在
if not os.path.exists('plots'):
    os.makedirs('plots')

# 指定端口号
FLASK_PORT = 5001

# 设置静态文件路由
@app.route('/')
def index():
    return send_from_directory('.', 'webui.html')

# 定义Python函数
def import_files_one():
    return "导入一个数组"

def import_files_two():
    return "导入两个数组"

def import_files_three():
    return "导入三个数组"

# 定义路由处理函数
@app.route('/call_function', methods=['POST'])
def call_function():
    function_name = request.json.get('function_name')
    if function_name == 'import_files_one':
        result = import_files_one()
        return jsonify({'result': result, 'url': url_for('one_page')})
    elif function_name == 'import_files_two':
        result = import_files_two()
        return jsonify({'result': result, 'url': url_for('two_page')})
    elif function_name == 'import_files_three':
        result = import_files_three()
        return jsonify({'result': result, 'url': url_for('three_page')})
    else:
        return jsonify({'result': "未知函数", 'url': None})

# 定义跳转页面路由
# 跳转到不同的HTML页面
@app.route('/one')
def one_page():
    return send_file('one_array.html')

@app.route('/one_input')
def one_input_page():
    return send_file('one_input.html')

@app.route('/two')
def two_page():
    return send_file('two_arrays.html')

@app.route('/two_inputs')
def two_inputs_page():
    return send_file('two_inputs.html')

@app.route('/three')
def three_page():
    return send_file('three_arrays.html')

@app.route('/three_inputs')
def three_inputs_page():
    return send_file('three_inputs.html')

# 处理图表请求
@app.route('/plot', methods=['POST'])
def plot():
    try:
        data = request.json
        print(f"接收到的数据: {data}")
        
        chart_type = data['chart_type']
        plot_type = data['type']
        print(f"图表类型: {chart_type}, 绘图类型: {plot_type}")
        
        if not isinstance(data['array1'], list):
            return jsonify({'success': False, 'error': '数据格式错误：array1 必须是数组'})
        
        # 将输入数据转换为数组
        try:
            array1 = np.array(data['array1'])
            print(f"array1: {array1}")
        except (ValueError, TypeError) as e:
            print(f"转换array1时出错: {e}")
            return jsonify({'success': False, 'error': '数据格式错误：array1 包含无效数值'})
            
        if chart_type == 'one_array':
            try:
                filename = None
                if plot_type == 'histogram':
                    filename = plot_histogram(array1)
                elif plot_type == 'box':
                    filename = plot_box(array1)
                elif plot_type == 'violin':
                    filename = plot_violin(array1)
                elif plot_type == 'bar':
                    x = np.arange(len(array1))
                    filename = plot_bar(x, array1)
                else:
                    return jsonify({'success': False, 'error': f'未知的图表类型：{plot_type}'})
                
                if not filename:
                    return jsonify({'success': False, 'error': '生成图片失败'})
            except Exception as e:
                print(f"绘制一维图表时出错: {e}")
                return jsonify({'success': False, 'error': str(e)})
        
        elif chart_type == 'two_arrays':
            # 验证array2是否为列表
            if not isinstance(data['array2'], list):
                return jsonify({'success': False, 'error': '数据格式错误：array2 必须是数组'})
            
            try:
                array2 = np.array(data['array2'])
                print(f"array2: {array2}")
            except (ValueError, TypeError) as e:
                print(f"转换array2时出错: {e}")
                return jsonify({'success': False, 'error': '数据格式错误：array2 包含无效数值'})
                
            # 检查两个数组长度是否相同
            if len(array1) != len(array2):
                print(f"数组长度不匹配: array1={len(array1)}, array2={len(array2)}")
                return jsonify({'success': False, 'error': '两个数组长度必须相同'})
                
            try:
                filename = None
                if plot_type == 'scatter':
                    filename = plot_scatter(array1, array2)
                elif plot_type == 'line':
                    filename = plot_line(array1, array2)
                elif plot_type == 'bar':
                    filename = plot_bar(array1, array2)
                else:
                    return jsonify({'success': False, 'error': f'未知的图表类型：{plot_type}'})
                
                if not filename:
                    return jsonify({'success': False, 'error': '生成图片失败'})
                print("图表生成成功")
            except Exception as e:
                print(f"绘制二维图表时出错: {e}")
                return jsonify({'success': False, 'error': str(e)})
        
        elif chart_type == 'three_arrays':
            # 验证array2和array3是否为列表
            if not isinstance(data['array2'], list) or not isinstance(data['array3'], list):
                return jsonify({'success': False, 'error': '数据格式错误：array2和array3必须是数组'})
            
            try:
                array2 = np.array(data['array2'])
                array3 = np.array(data['array3'])
                print(f"array2: {array2}")
                print(f"array3: {array3}")
            except (ValueError, TypeError) as e:
                print(f"转换array2或array3时出错: {e}")
                return jsonify({'success': False, 'error': '数据格式错误：array2或array3包含无效数值'})
            
            # 检查三个数组长度是否相同
            if not (len(array1) == len(array2) == len(array3)):
                print(f"数组长度不匹配: array1={len(array1)}, array2={len(array2)}, array3={len(array3)}")
                return jsonify({'success': False, 'error': '三个数组长度必须相同'})
            
            try:
                filename = None
                if plot_type == 'scatter3d':
                    filename = plot_scatter3d(array1, array2, array3)
                elif plot_type == 'line3d':
                    filename = plot_line3d(array1, array2, array3)
                elif plot_type == 'bar3d':
                    filename = plot_bar3d(array1, array2, array3)
                else:
                    return jsonify({'success': False, 'error': f'未知的三维图表类型：{plot_type}'})
                
                if not filename:
                    return jsonify({'success': False, 'error': '生成图片失败'})
                print("三维图表生成成功")
            except Exception as e:
                print(f"绘制三维图表时出错: {e}")
                return jsonify({'success': False, 'error': str(e)})

        # 返回成功响应
        return jsonify({
            'success': True,
            'message': '图表生成成功',
            'image_url': f'/plots/{filename}'
        })

    except Exception as e:
        print(f"处理请求时出错: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# 确保图片文件可以被访问
@app.route('/plots/<path:filename>')
def serve_plots(filename):
    return send_from_directory('plots', filename)

# 添加跨域支持的错误处理
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response

def open_browser():
    time.sleep(1.5)  # 等待服务器启动
    print(f"\n请在 VS Code 中使用以下方式访问网页：")
    print(f"1. 按下 Cmd/Ctrl + Shift + P")
    print(f"2. 输入 'Simple Browser: Show'")
    print(f"3. 在弹出的输入框中输入: http://localhost:{FLASK_PORT}")
    print(f"\n或者直接点击这个链接：http://localhost:{FLASK_PORT}")

if __name__ == '__main__':
    # 启动浏览器提示的线程
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # 启动Flask服务器
    print(f"Flask Server started at http://localhost:{FLASK_PORT}")
    app.run(host='0.0.0.0', port=FLASK_PORT, debug=False)
