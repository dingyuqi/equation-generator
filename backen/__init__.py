import sys
from PySide2 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets
import socket


class ApplicationThread(QtCore.QThread):
    def __init__(self, application, port=5000):
        super(ApplicationThread, self).__init__()
        self.application = application
        self.port = port

    def __del__(self):
        self.wait()

    def run(self):
        # flask app.run()
        self.application.run(port=self.port, threaded=True)


class WebPage(QtWebEngineWidgets.QWebEnginePage):
    def __init__(self, root_url):
        super(WebPage, self).__init__()
        self.root_url = root_url

    def home(self):
        self.load(QtCore.QUrl(self.root_url))


def init_gui(application, icon, port, width=800, height=600,
             window_title="PyFladesk", argv=None):
    if argv is None:
        argv = sys.argv

    # 创建主窗口框架
    qtapp = QtWidgets.QApplication(argv)

    # 线程启动flask
    webapp = ApplicationThread(application, port)
    webapp.start()
    # connect function:关闭qtapp窗口时，调用flask的终止
    qtapp.aboutToQuit.connect(webapp.terminate)

    # 创建主窗口，并设置大小，标题，icon
    window = QtWidgets.QMainWindow()
    window.resize(width, height)
    window.setWindowTitle(window_title)
    window.setWindowIcon(QtGui.QIcon(icon))

    # 创建WebEngineView并套入主窗口
    webView = QtWebEngineWidgets.QWebEngineView(window)
    window.setCentralWidget(webView)

    # 通过home()加载url,并将page放入view
    page = WebPage('http://localhost:{}'.format(port))
    page.home()
    webView.setPage(page)

    # 显示窗口
    window.show()
    # 进入程序的主循环直到exit()被调用
    return qtapp.exec_()

