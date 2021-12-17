import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from pythonProject.query_window import Ui_MainWindow
from pythonProject.specialization import Ui_MainWindow_Specialization


class ResultWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, town, f_subject, s_subject, t_subject, summ):
        super().__init__()
        self.town = town
        self.f_subject = f_subject
        self.s_subject = s_subject
        self.t_subject = t_subject
        self.summ = summ
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton__query_window_univ.clicked.connect(lambda: self.hide())
        connection = sqlite3.connect("BD.db")
        cursor = connection.cursor()
        if self.town != "Любой":
            university = cursor.execute(f"""SELECT title_university FROM university WHERE city = "{self.town}" """).fetchall()
            university = list(map(lambda j: str(j)[1:(len(str(j)) - 2):], university))
        else:
            university = cursor.execute("""SELECT title_university FROM university""").fetchall()
            university = list(map(lambda j: str(j)[1:(len(str(j)) - 2):], university))
        university_id = []
        for j in range(len(university)):
            university__id = cursor.execute(
                f"""SELECT id_university FROM university WHERE title_university = {university[j]} """).fetchone()
            university_id.append(str(university__id)[1: (len(university__id) - 3)])
        specialization_id = []
        predmet_id = []
        predmet_id_selected = []
        if self.f_subject != "Любой" or self.s_subject != "Любой" or self.t_subject != "Любой":
            for j in range(len(university_id)):
                specialization__id = cursor.execute(
                    f"""SELECT id_specialization FROM university_specialization WHERE id_university = {int(university_id[j])} """).fetchall()
                specialization_id.append(list(map(lambda p: str(p)[1:(len(str(p)) - 2):], specialization__id)))
            for j in range(len(specialization_id)):
                predmet_id.append([])
                for t in range(len(specialization_id[j])):
                    predmet__id = cursor.execute(
                        f"""SELECT id_subject FROM specialization_subject WHERE id_specialization = {int(specialization_id[j][t])} """).fetchall()
                    predmet_id[j].append(list(map(lambda p: str(p)[1:(len(str(p)) - 2):], predmet__id)))
            if self.f_subject != "Любой":
                selected = cursor.execute(
                f"""SELECT id_subject FROM subject WHERE title_subject = "{self.f_subject}" """).fetchone()
                predmet_id_selected.append(str(selected)[1: (len(selected) - 3)])
            if self.s_subject != "Любой":
                selected = cursor.execute(
                f"""SELECT id_subject FROM subject WHERE title_subject = "{self.s_subject}" """).fetchone()
                predmet_id_selected.append(str(selected)[1: (len(selected) - 3)])
            if self.t_subject != "Любой":
                selected = cursor.execute(
                f"""SELECT id_subject FROM subject WHERE title_subject = "{self.t_subject}" """).fetchone()
                predmet_id_selected.append(str(selected)[1: (len(selected) - 3)])
        spec = []
        for i in range(len(predmet_id)):
            spec.append([])
            for j in range(len(predmet_id[i])):
                P = True
                if len(predmet_id[i][j]) >= len(predmet_id_selected):
                    for elem in predmet_id_selected:
                        if elem not in predmet_id[i][j]:
                            P = False
                else:
                    for elem in predmet_id[i][j]:
                        if elem not in predmet_id_selected:
                            P = False
                if P:
                    spec[i].append(predmet_id[i][j])
                else:
                    spec[i].append([])
        for i in range(len(spec)):
            for j in range(len(spec[i])):
                if not spec[i][j]:
                    specialization_id[i][j] = ""
        university_1 = []
        if self.summ != "":
            if not specialization_id and len(university_id) == 18:
                summa = cursor.execute(
                        f"""SELECT id_university, id_specialization FROM university_specialization WHERE total_score <= {int(self.summ)} """).fetchall()
                summa = list(map(lambda p: str(p)[1:(len(str(p)) - 1)], summa))
                university_id = list(set(map(lambda x: str(x).split(", ")[0], summa)))
                for i, elem in enumerate(university_id):
                    specialization_id.append([])
                    for st in summa:
                        if st.split(", ")[0] == elem:
                            specialization_id[i].append(st.split(", ")[1])
            elif not specialization_id and len(university_id) != 18:
                for i in range(len(university_id)):
                    summa = cursor.execute(
                        f"""SELECT id_specialization FROM university_specialization WHERE total_score <= {int(self.summ)} AND id_university = {int(university_id[i])}""").fetchall()
                    summa = list(map(lambda p: str(p)[1:(len(str(p)) - 2)], summa))
                    if not summa:
                        specialization_id.append([""])
                    else:
                        specialization_id.append(summa)
            else:
                for i in range(len(specialization_id)):
                    for j in range(len(specialization_id[i])):
                        if specialization_id[i][j] != "":
                            summa = cursor.execute(
                                f"""SELECT total_score FROM university_specialization WHERE id_specialization = {int(specialization_id[i][j])} AND id_university = {int(university_id[i])}""").fetchone()
                            summa = str(summa)[1:(len(str(summa)) - 2)]
                            if int(summa) > int(self.summ):
                                specialization_id[i][j] = ""
        for i in range(len(specialization_id)):
            if set(specialization_id[i]) == {""}:
                university_id[i] = ""
        for i in range(len(university_id)):
            if university_id[i] != "":
                university__1 = cursor.execute(
                    f"""SELECT title_university FROM university WHERE id_university = {int(university_id[i])} """).fetchone()
                university_1.append(str(university__1)[1: (len(university__1) - 3)])
            else:
                university_1.append("")
        self.university_id = university_id
        self.spec = specialization_id
        x = 20
        y = 40
        lst = []
        for i in range(len(university_1)):
            if university_1[i] != "":
                text = cursor.execute(
                    f"""SELECT city FROM university WHERE id_university = {int(university_id[i])} """).fetchone()
                text = str(text)[1:(len(str(text)) - 2)]
                self.label = QLabel(self)
                self.label.setText(university_1[i] + "\n" + text)
                self.pushButton = QPushButton(self)
                self.pushButton.setGeometry(x, y, 860, 40)
                self.pushButton.setText(self.label.text())
                self.label.setText("")
                self.pushButton.setObjectName(f"pushButton_{i}")
                y += 50
                lst.append(self.pushButton)
        for button in lst:
            button.clicked.connect(self.specialization)

    def specialization(self):
        id = self.sender().objectName()
        self.wnd_create = Specialization(self.university_id, id, self.spec)
        self.wnd_create.show()


class Specialization(QMainWindow, Ui_MainWindow_Specialization):
    def __init__(self, university_id, id, spec):
        super().__init__()
        self.setupUi(self)
        self.university_id = university_id
        self.spec = spec
        self.id = int(id[11:])
        self.initUi()

    def initUi(self):
        self.pushButton_specialization.clicked.connect(lambda: self.hide())
        connection = sqlite3.connect("BD.db")
        cursor = connection.cursor()
        x = 20
        y = 40
        if not self.spec:
            self.spec = []
            for i in range(self.id + 1):
                if i == self.id:
                    text_1 = cursor.execute(
                        f"""SELECT id_specialization FROM university_specialization WHERE id_university = {int(self.university_id[self.id])} """).fetchall()
                    self.spec.append(list(map(lambda p: str(p)[1:(len(str(p)) - 2):], text_1)))
                else:
                    self.spec.append([])
        for elem in self.spec[self.id]:
            if elem != "":
                text = cursor.execute(
            f"""SELECT title_specialization FROM specialization WHERE id_specialization = {int(elem)} """).fetchone()
                text = str(text)[1: (len(text) - 3)]
                text_2 = cursor.execute(
            f"""SELECT total_score FROM university_specialization WHERE id_specialization = {int(elem)} AND id_university = {int(self.university_id[self.id])} """).fetchone()
                text_2 = str(text_2)[1: (len(text_2) - 3)]
                self.lable = QLabel(self)
                self.lable.setGeometry(x, y, 640, 40)
                self.lable.setText(text + "\n сумма баллов для поступления: " + text_2)
                self.lable.setObjectName(f"pushButton")
                y += 50


class RequestHistoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        pass