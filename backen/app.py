import json

from flask import Flask, render_template, request, make_response, jsonify

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
        if data["file_path"]:  # 判断是否为空
            return jsonify({
                'code': 200,
                'data': "",
                'msg': 'success'})
        else:
            return jsonify({
                'code': 404,
                'data': "",
                'msg': 'failed'})
