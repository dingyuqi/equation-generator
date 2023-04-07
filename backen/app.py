from flask import Flask, render_template, request, make_response, jsonify

app = Flask(__name__, static_url_path='', static_folder='../front', template_folder='../front')

app.config['EXPLAIN_TEMPLATE_LOADING'] = True


# 路由
@app.route('/')
def greet():
    return render_template("login.html")


@app.route('/run', methods=['POST'])
def run():
    print("!!!!!!!!!!!!!", request.method, request.method == "POST", request.get_json())
    if request.method == "POST":
        print("1111", request.get_json())
        if request.get_json()["file_path"]:  # 判断是否为空
            print("2222", request.get_json()["file_path"], "=========")
            return jsonify({'status': True})
