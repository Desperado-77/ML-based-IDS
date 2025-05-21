# use pyside6, i need a frameless window, but it should be draggable, resizable, and customer title bar
import textwrap
import traceback

from PySide6.QtCore import Qt, QThread, QThreadPool, QRunnable, QObject, Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QRadioButton, \
    QButtonGroup, QFileDialog, QFrame, QComboBox, QGridLayout
from qframelesswindow import FramelessWindow
import data_mining
from ui_window import Ui_Form


class WorkerSignal(QObject):
    result = Signal(str, str)
    start = Signal(bool)


class Runner(QRunnable):
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.worker = WorkerSignal()
        super().__init__()

    def run(self):
        self.worker.start.emit(True)
        try:
            res = str(self.func(*self.args, **self.kwargs))
            result = res, "success"
        except Exception as e:
            traceback.print_exc()
            result = str(e), "error"

        self.worker.result.emit(*result)


class Application(FramelessWindow, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setObjectName("app")
        self.current_pixmap = None  # 存储当前的 pixmap 对象
        self.resize(1100, 700)
        self.setWindowTitle("PyQt-Frameless-Window")
        self.titleBar.raise_()
        # self.titleBar.setFixedHeight(40)
        title = QLabel("基于机器学习的入侵检测系统")
        title.setObjectName("title")
        label_logo = QLabel()
        label_logo.setObjectName("logo")
        label_logo.setPixmap(QIcon("./img/logo.png").pixmap(32, 32))
        self.titleBar.hBoxLayout.insertStretch(0, 1)
        self.titleBar.hBoxLayout.insertWidget(1, title, 0, Qt.AlignCenter)
        self.titleBar.hBoxLayout.insertStretch(2, 1)
        self.titleBar.hBoxLayout.insertWidget(3, label_logo, 0, Qt.AlignCenter)

        with open("./style.qss", "r") as f:
            self.setStyleSheet(f.read())

        # 按钮组
        self.buttonGroup1 = QButtonGroup()
        self.buttonGroup1.addButton(self.pushButton_1, 1)
        self.buttonGroup1.addButton(self.pushButton_2, 2)
        self.buttonGroup1.addButton(self.pushButton_3, 3)
        self.buttonGroup1.addButton(self.pushButton_4, 4)
        self.buttonGroup1.addButton(self.pushButton_5, 5)
        self.buttonGroup1.addButton(self.pushButton_6, 6)

        self.buttonGroup2 = QButtonGroup()
        self.buttonGroup2.addButton(self.radioButton, 1)
        self.radioButton.setChecked(True)
        self.buttonGroup2.addButton(self.radioButton_2, 2)
        self.buttonGroup2.addButton(self.radioButton_3, 3)

        self.buttonGroup1.idClicked.connect(self._data_switch)

        self.buttonGroup2.idClicked.connect(self._model_switch)
        self.model = 1  # 1， 2， 3 分别对应三种模式
        # 添加选项
        self.comboBox.addItems(SELECTED)
        self.selected = 1  # 选项值
        self.comboBox.currentIndexChanged.connect(self._selected)
        self.comboBox.setCurrentIndex(0)

        self.current_file = None

        self.pushButton_8.clicked.connect(self.go1)
        self.pushButton_9.clicked.connect(self.go2)
        self.pushButton_10.clicked.connect(self.go3)
        self.pushButton_11.clicked.connect(self.go4)

        self.thread_pool = QThreadPool(self)

    def process_results(self, result, status):
        print(result, status)
        if status == "success":
            if result.endswith(".png"):
                # 更新当前的 pixmap 对象
                self.current_pixmap = QPixmap(result).scaledToWidth(self.lable_show.width(),
                                                                    Qt.SmoothTransformation)
                self.lable_show.setPixmap(self.current_pixmap)
            else:
                self.lable_show.setText("\n".join(v.strip() for v in result.split("\n")))

    def start_task(self, status):
        if status:
            # pixmap 为空
            self.lable_show.setPixmap(QPixmap())
            self.lable_show.setText("正在处理中...")

    def _data_switch(self, pk):
        func = None
        if pk == 1:
            func = self.data1
        elif pk == 2:
            func = self.data2
        elif pk == 3:
            func = self.data3
        elif pk == 4:
            func = self.data4
        elif pk == 5:
            func = self.data5
        elif pk == 6:
            func = self.data6
        if func:
            worker = Runner(func)
            worker.worker.start.connect(self.start_task)
            worker.worker.result.connect(self.process_results)
            self.thread_pool.start(worker)

    def _model_switch(self, pk):
        # self.model = pk
        self.model = pk
        print("模式：", pk, self.buttonGroup2.button(pk).text())

    def _selected(self, pk):
        self.selected = pk
        print("选项：", pk, self.selected)

    def _open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "./", "Model file (*.pt)")
        if file_name:
            self.current_file = file_name
            print("选择文件：", file_name)

    def data1(self):  # 这是界面上按钮1的功能
        print("按钮1")
        return data_mining.button1()

    def data2(self):  # 这是界面上按钮2的功能
        print("按钮2")
        return data_mining.button2()

    def data3(self):
        print("按钮3")
        return data_mining.button3()

    def data4(self):
        print("按钮4")
        return data_mining.button4()

    def data5(self):
        print("按钮5")
        return data_mining.button5()

    def data6(self):
        print("按钮6")
        return data_mining.button6()

    def go1(self):  # 这是界面上按钮第一个 GO 的功能
        print("GO1")
        # print(self.model)
        # return data_mining.button1()
        func = None
        if self.model == 1:
            func = data_mining.m1
        elif self.model == 2:
            func = data_mining.m2
        elif self.model == 3:
            func = data_mining.m3
        if func:
            worker = Runner(func)
            worker.worker.start.connect(self.start_task)
            worker.worker.result.connect(self.process_results)
            self.thread_pool.start(worker)

    def go2(self):  # 这是界面上按钮第二个 GO 的功能
        print("GO2")
        print(self.selected)
        func = None
        if self.selected == 0:
            func = data_mining.matrix1
        elif self.selected == 1:
            func = data_mining.matrix2
        elif self.selected == 2:
            func = data_mining.matrix3
        if func:
            worker = Runner(func)
            worker.worker.start.connect(self.start_task)
            worker.worker.result.connect(self.process_results)
            self.thread_pool.start(worker)

    def go3(self):  # 这是界面上按钮第三个 GO 的功能
        print("GO3")
        data_mining.comparison1()
        worker = Runner(data_mining.comparison1)
        worker.worker.start.connect(self.start_task)
        worker.worker.result.connect(self.process_results)
        self.thread_pool.start(worker)

    def go4(self):  # 这是界面上按钮第四个 GO 的功能
        print("GO4")
        data_mining.comparison2()        
        worker = Runner(data_mining.comparison2)
        worker.worker.start.connect(self.start_task)
        worker.worker.result.connect(self.process_results)
        self.thread_pool.start(worker)


if __name__ == '__main__':
    app = QApplication([])
    SELECTED = ["决策树", "逻辑回归", "人工神经网络"]
    window = Application(None)
    window.show()
    app.exec()
