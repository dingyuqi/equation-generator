import json
import os
import sys

from PySide2 import QtWidgets, QtWebEngineWidgets
from PySide2.QtWidgets import QFileDialog
from flask import Flask, render_template, request, jsonify

from backen.generat_equation import write_excel, generate_equations

app = Flask(__name__, static_url_path='', static_folder='../front', template_folder='../front')

app.config['EXPLAIN_TEMPLATE_LOADING'] = True


# 路由
@app.route('/')
def greet():
    return render_template("login.html")


@app.route('/run', methods=['POST'])
def run():
    if request.method == "POST":
        data = json.loads(request.get_data())
        print(data)
        if data["dir_path"]:  # 判断是否为空
            dir_path = data["dir_path"]
            operator = data["operator"]
            min_num = data["min"]
            max_num = data["max"]
            num_terms = data["num_terms"]
            try:
                write_excel(dir_path, generate_equations(50, operator, min_num, max_num, num_terms))
            except Exception as e:
                return jsonify({
                    "code": 404,
                    "data": None,
                    "msg": e})
            return jsonify({
                "code": 200,
                "data": None,
                "msg": "生成成功"})
        else:
            return jsonify({
                "code": 404,
                "data": None,
                "msg": "请先选择路径"})


@app.route('/file', methods=['POST'])
def open_file():
    class MyWindow(QtWidgets.QWidget):
        def msg(self):
            directory1 = QFileDialog.getExistingDirectory(self,
                                                          "选取文件夹",
                                                          "./")  # 起始路径
            print(directory1)
            return directory1

    myshow = MyWindow()
    dir_path = myshow.msg()

    return jsonify({"code": 200, "msg": "", "data": dir_path})


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000, threaded=True)
