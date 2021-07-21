# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from scoreboard import Ui_Dialog as Score  # Score window
import sqlite3
match = sqlite3.connect("fantasy.db")
matchcur = match.cursor()


class Ui_evaluate_team(object):
    def __init__(self):  # initialising score window
        self.scoreDialog = QtWidgets.QMainWindow()
        self.score_screen = Score()
        self.score_screen.setupUi(self.scoreDialog)

    def setupUi(self, evaluate_team):
        evaluate_team.setObjectName("evaluate_team")
        evaluate_team.resize(634, 504)
        evaluate_team.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.label = QtWidgets.QLabel(evaluate_team)
        self.label.setGeometry(QtCore.QRect(90, 20, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.selectteam_cb = QtWidgets.QComboBox(evaluate_team)
        self.selectteam_cb.setGeometry(QtCore.QRect(90, 70, 141, 21))
        self.selectteam_cb.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "font: 75 italic 10pt \"Arial\";")
        self.selectteam_cb.setObjectName("selectteam_cb")
        self.selectteam_cb.addItem("")
        self.selectmatch_cb = QtWidgets.QComboBox(evaluate_team)
        self.selectmatch_cb.setEnabled(True)
        self.selectmatch_cb.setGeometry(QtCore.QRect(360, 70, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.selectmatch_cb.setFont(font)
        self.selectmatch_cb.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "font: 75 italic 11pt \"Arial\";")
        self.selectmatch_cb.setObjectName("selectmatch_cb")
        self.selectmatch_cb.addItem("")
        self.selectmatch_cb.addItem("")
        self.line = QtWidgets.QFrame(evaluate_team)
        self.line.setGeometry(QtCore.QRect(40, 95, 551, 41))
        self.line.setStyleSheet("color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(evaluate_team)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(evaluate_team)
        self.label_3.setGeometry(QtCore.QRect(350, 150, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.calcscore_btn = QtWidgets.QPushButton(evaluate_team)
        self.calcscore_btn.setEnabled(True)
        self.calcscore_btn.setGeometry(QtCore.QRect(240, 410, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.calcscore_btn.setFont(font)
        self.calcscore_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.calcscore_btn.setAutoDefault(False)
        self.calcscore_btn.setObjectName("calcscore_btn")
        self.players_lw = QtWidgets.QListWidget(evaluate_team)
        self.players_lw.setGeometry(QtCore.QRect(80, 180, 191, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.players_lw.setFont(font)
        self.players_lw.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.players_lw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.players_lw.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.players_lw.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.players_lw.setObjectName("players_lw")
        self.scores_lw = QtWidgets.QListWidget(evaluate_team)
        self.scores_lw.setGeometry(QtCore.QRect(340, 180, 191, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scores_lw.setFont(font)
        self.scores_lw.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scores_lw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scores_lw.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.scores_lw.setObjectName("scores_lw")

        self.retranslateUi(evaluate_team)
        QtCore.QMetaObject.connectSlotsByName(evaluate_team)

        self.calcscore_btn.clicked.connect(self.final_score)
        selected_team = self.selectteam_cb.currentText()

        self.changedname(selected_team)
        self.selectteam_cb.currentTextChanged.connect(self.changedname)

    def retranslateUi(self, evaluate_team):
        _translate = QtCore.QCoreApplication.translate
        evaluate_team.setWindowTitle(_translate("evaluate_team", "Dialog"))
        self.label.setText(_translate(
            "evaluate_team", "Evaluate the Performance of your Fantasy Team"))
        self.selectteam_cb.setCurrentText(
            _translate("evaluate_team", "Select team"))
        self.selectteam_cb.setItemText(
            0, _translate("evaluate_team", "Select team"))
        self.selectmatch_cb.setItemText(
            0, _translate("evaluate_team", "select match"))
        self.selectmatch_cb.setItemText(
            1, _translate("evaluate_team", "Match1"))
        self.label_2.setText(_translate("evaluate_team", "Players"))
        self.label_3.setText(_translate("evaluate_team", "Points"))
        self.calcscore_btn.setStatusTip(
            _translate("evaluate_team", "calculating score"))
        self.calcscore_btn.setText(_translate(
            "evaluate_team", "Calculate Score"))
        x = matchcur.execute("SELECT  DISTINCT name from teams;")
        team = x.fetchall()
        for i in team:
            self.selectteam_cb.addItem(i[0])

    def changedname(self, t):
        self.players_lw.clear()
        self.scores_lw.clear()
        y = matchcur.execute(
            "SELECT players from teams WHERE name='" + t + "';")
        player = y.fetchall()

        # print('player',player)
        for j in player:
            self.players_lw.addItem(j[0])
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()
        for k in value:
            self.scores_lw.addItem(str(k[0]))

    def final_score(self):
        total_score = 0
        t = self.selectteam_cb.currentText()   # current teamname
        # print(t)
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()

        # print('value', value)
        for k in value:
            total_score += k[0]
        # opening score dialog box and setting final score
        self.score_screen.finalscore.setText(str(total_score))
        self.scoreDialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluate_team = QtWidgets.QDialog()
    ui = Ui_evaluate_team()
    ui.setupUi(evaluate_team)
    evaluate_team.show()
    sys.exit(app.exec_())
