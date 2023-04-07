from flask import Flask,  render_template

app = Flask(__name__, static_url_path='', static_folder='../front', template_folder='../front')


app.config['EXPLAIN_TEMPLATE_LOADING'] = True

# 路由
@app.route('/')
def greet():
    return render_template("login.html")


