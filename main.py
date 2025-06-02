from flask import Flask, request, jsonify, redirect, url_for, send_from_directory
import webbrowser
import threading
import time
import os
from flask import send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
@app.route('/one')
def one_page():
    return send_file('one_array.html')

@app.route('/two')
def two_page():
    return send_file('two_arrays.html')

@app.route('/three')
def three_page():
    return send_file('three_arrays.html')

# Safari is inavailable on macOS, so we will use Chrome or Firefox
def open_browser_via_chrome():
    time.sleep(1.5)  # 等待服务器启动
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    browser = webbrowser.get(chrome_path)
    browser.open(f'http://localhost:{FLASK_PORT}')

# open firefox if chrome is not available
def open_browser_via_firefox():
    time.sleep(1.5)  # 等待服务器启动
    firefox_path = 'open -a /Applications/Firefox.app %s'
    browser = webbrowser.get(firefox_path)
    browser.open(f'http://localhost:{FLASK_PORT}')

if __name__ == '__main__':
    # 启动浏览器的线程
    browser_thread = threading.Thread(target=open_browser_via_chrome)
    #当chrome不可用时，使用Firefox
    if not webbrowser.get('chrome'):
        browser_thread = threading.Thread(target=open_browser_via_firefox)
    # 设置线程为守护线程
    browser_thread.daemon = True
    browser_thread.start()
    
    # 启动Flask服务器
    print(f"Flask Server started at http://localhost:{FLASK_PORT}")
    app.run(host='0.0.0.0', port=FLASK_PORT, debug=False)

