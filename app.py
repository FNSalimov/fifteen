from PyQt4 import QtGui, QtCore
import sys, os
import fifteen, random
from functools import partial

class App(QtGui.QMainWindow, fifteen.Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.setFocus(True)
        exit = QtGui.QAction('Exit', self)
        exit.setShortcut('Ctrl+Q')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        mix = QtGui.QAction('Mix', self)
        mix.setShortcut('Ctrl+D')
        QtCore.QObject.connect(mix, QtCore.SIGNAL('triggered()'), self.contribution)
        finish = QtGui.QAction('Finish', self)
        finish.setShortcut('Ctrl+F')
        QtCore.QObject.connect(finish, QtCore.SIGNAL('triggered()'), self.finish)
        about = QtGui.QAction('About app', self)
        about.setShortcut('Ctrl+O')
        QtCore.QObject.connect(about, QtCore.SIGNAL('triggered()'), self.about)
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(mix)
        file.addAction(finish)
        file.addAction(about)
        file.addAction(exit)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.show()
        self.my_dict = {1: self.pushButton, 2: self.pushButton_2, 3: self.pushButton_3,
        4: self.pushButton_4, 5: self.pushButton_5, 6: self.pushButton_6, 7: self.pushButton_7,
        8: self.pushButton_8, 9: self.pushButton_9, 10: self.pushButton_10,
        11: self.pushButton_11, 12: self.pushButton_12, 13: self.pushButton_13,
        14: self.pushButton_14, 15: self.pushButton_15}
        self.list_of_buttons = []
        for i in range(1, 16):
            self.my_dict[i].setFont(font)
            self.list_of_buttons.append(self.my_dict[i])
            QtCore.QObject.connect(self.my_dict[i], QtCore.SIGNAL("clicked()"), partial(self.foo, i))
        self.time_id = self.startTimer(1000)
        self.seconds, self.minutes = 0, 0
        self.contribution()
    def foo(self, number):
        self.x, self.y = 0, 0
        if self.label.x() == self.my_dict[number].x() + 60 and self.label.y() == self.my_dict[number].y():
            self.label.move(self.label.x() - 60, self.label.y())
            self.my_dict[number].move(self.my_dict[number].x() + 60, self.label.y())
        elif self.label.x() == self.my_dict[number].x() - 60 and self.label.y() == self.my_dict[number].y():
            self.label.move(self.label.x() + 60, self.label.y())
            self.my_dict[number].move(self.my_dict[number].x() - 60, self.label.y())
        elif self.label.y() == self.my_dict[number].y() - 60 and self.label.x() == self.my_dict[number].x():
            self.label.move(self.label.x(), self.label.y() + 60)
            self.my_dict[number].move(self.my_dict[number].x(), self.my_dict[number].y() - 60)
        elif self.label.y() == self.my_dict[number].y() + 60 and self.label.x() == self.my_dict[number].x():
            self.label.move(self.label.x(), self.label.y() - 60)
            self.my_dict[number].move(self.my_dict[number].x(), self.my_dict[number].y() + 60)
        self.setFocus(True)
        self.check()
    def contribution(self):
        new_dict = {}
        for i in range(15):
            new_dict[self.my_dict[i + 1]] = i + 1
        random.shuffle(self.list_of_buttons)
        check_list = []
        for i in range(15):
            check_list.append(new_dict[self.list_of_buttons[i]])
        result = 0
        for i in range(15):
            for j in range(i, 15):
                if check_list[i] > check_list[j]:
                    result += 1
        if result % 2 == 1:
            self.contribution()
        self.x, self.y = 0, 0
        for i in range(15):
            if i == 4 or i == 8 or i == 12:
                self.x = 0
                self.y += 60
            self.list_of_buttons[i].move(self.x, self.y)
            self.x += 60
        self.label.move(180, 180)
        self.minutes, self.seconds = 0, 0
    def finish(self):
        self.x, self.y = 0, 0
        for i in range(1, 16):
            if i == 5 or i == 9 or i == 13:
                self.x = 0
                self.y += 60
            self.my_dict[i].move(self.x, self.y)
            self.x += 60
        self.label.move(180, 180)
        QtGui.QMessageBox.information(self, "Congratulations!", "You have done it :-), Result: "
                    + str(self.minutes) + " minutes and " + str(self.seconds) + " seconds", QtGui.QMessageBox.Ok)
        self.minutes, self.seconds = 0, 0
    def check(self):
        self.x, self.y = 0, 0
        for i in range(1, 16):
            #print(self.my_dict[i].x(), self.x, self.my_dict[i].y(), self.y)
            if i == 5 or i == 9 or i == 13:
                self.x = 0
                self.y += 60
            if self.my_dict[i].x() != self.x or self.my_dict[i].y() != self.y:
                #print("NO!!!!")
                break
            self.x += 60
            if i == 15:
                #print("YES!!!")
                QtGui.QMessageBox.information(self, "Congratulations!", "You have done it :-), Result: "
                    + str(self.minutes) + " minutes and " + str(self.seconds) + " seconds", QtGui.QMessageBox.Ok)
                self.minutes, self.seconds = 0, 0
    def keyPressEvent(self, event):
        if event.key() == 16777234:
            for i in range(1, 16):
                if self.my_dict[i].y() == self.label.y() and self.my_dict[i].x() == self.label.x() + 60:
                    self.my_dict[i].move(self.my_dict[i].x() - 60, self.my_dict[i].y())
                    self.label.move(self.label.x() + 60, self.label.y())
                    self.check()
                    break
        elif event.key() == 16777235:
            for i in range(1, 16):
                if self.my_dict[i].x() == self.label.x() and self.my_dict[i].y() == self.label.y() + 60:
                    self.my_dict[i].move(self.my_dict[i].x(), self.my_dict[i].y() - 60)
                    self.label.move(self.label.x(), self.label.y() + 60)
                    self.check()
                    break
        elif event.key() == 16777236:
            for i in range(1, 16):
                if self.my_dict[i].y() == self.label.y() and self.my_dict[i].x() == self.label.x() - 60:
                    self.my_dict[i].move(self.label.x(), self.my_dict[i].y())
                    self.label.move(self.label.x() - 60, self.label.y())
                    self.check()
                    break
        elif event.key() == 16777237:
            for i in range(1, 16):
                if self.my_dict[i].x() == self.label.x() and self.my_dict[i].y() == self.label.y() - 60:
                    self.my_dict[i].move(self.my_dict[i].x(), self.my_dict[i].y() + 60)
                    self.label.move(self.label.x(), self.label.y() - 60)
                    self.check()
                    break
    def about(self):
        QtGui.QMessageBox.about(self, "About Fifteen-app", '''Developer: Firdavs Salimov
email: firdavs_20111@mail.ru
16.05.2016''')
    def timerEvent(self, event):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        tmp = str(self.minutes)
        tmp_2 = str(self.seconds)
        if len(tmp) == 1:
            tmp = '0' + tmp
        if len(tmp_2) == 1:
            tmp_2 = '0' + tmp_2
        self.label.setText(tmp + ':' + tmp_2)
def main():
    app = QtGui.QApplication(sys.argv)
    form = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
