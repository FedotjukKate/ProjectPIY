from PyQt5.QtWidgets import QApplication, QMainWindow
from pythonProject.error_window import Ui_MainWindow_Error
from pythonProject.list_univ import Ui_MainWindow_Univ
from pythonProject.list_spec import Ui_MainWindow_Spec
from pythonProject.exit_window import Ui_MainWindow_Exit


class ExitWindow(QMainWindow, Ui_MainWindow_Exit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_exit_cancel.clicked.connect(lambda: self.hide())


class ErrorWindow(QMainWindow, Ui_MainWindow_Error):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class RequestHistory(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        pass


class List_Univ_Window(QMainWindow, Ui_MainWindow_Univ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_list_univ.clicked.connect(lambda: self.hide())


class List_Spec_Window(QMainWindow, Ui_MainWindow_Spec):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_list_spec.clicked.connect(lambda: self.hide())