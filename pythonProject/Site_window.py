import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from pythonProject.site_page import Ui_MainWindow_1
from pythonProject.Result_and_history import ResultWindow
from pythonProject.For_site_page import ExitWindow, ErrorWindow, List_Univ_Window, List_Spec_Window


class SiteWindow(QMainWindow, Ui_MainWindow_1):
    def __init__(self, user_id):
        super().__init__()
        self.id = int(user_id)
        self.setupUi(self)
        self.initUi()
        connection = sqlite3.connect("Registration_db.db")
        cursor = connection.cursor()
        user_name = cursor.execute(f"""SELECT user_name FROM User WHERE user_id = "{int(self.id)}" """).fetchone()
        user_name = str(user_name)[2: (len(user_name) - 4)]
        self.label_8.setText(user_name)

    def initUi(self):
        self.search_pushButton.clicked.connect(self.search)
        self.exit_pushButton.clicked.connect(self.exit)
        self.available_uni_pushButton.clicked.connect(self.List_univ)
        self.specialty_pushButton.clicked.connect(self.List_spec)

    def search(self):
        town, first_subject = self.town_comboBox.currentText(), self.subject_comboBox_1.currentText(),
        second_subject, third_subject = self.subject_comboBox_2.currentText(), self.subject_comboBox_3.currentText()
        summ = self.sum_textEdit.toPlainText()
        if town != "Любой" or first_subject != "Любой" or second_subject != "Любой"\
                or third_subject != "Любой" or summ != "":
            self.result(town, first_subject, second_subject, third_subject, summ)
        else:
            self.error()

    def List_univ(self):
        self.wnd_create = List_Univ_Window()
        self.wnd_create.show()

    def List_spec(self):
        self.wnd_create = List_Spec_Window()
        self.wnd_create.show()

    def error(self):
        self.wnd_create = ErrorWindow()
        self.wnd_create.show()

    def exit(self):
        self.wnd_create = ExitWindow()
        self.wnd_create.show()

    def result(self, t, f_s, s_s, th_s, summ):
        self.wnd_create = ResultWindow(t, f_s, s_s, th_s, summ)
        self.wnd_create.show()