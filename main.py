from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def application():
    app = QApplication(sys.argv) #создание приложения
    window = QMainWindow() #создание окна

    window.setWindowTitle('App') #титульник окна
    window.setGeometry(0, 0, 350, 200) #добавление окна (сдвиг по х, по у, ширина, высота)

    window.show() #показывает окно
    sys.exit(app.exec_()) #правильное завершение программы

if __name__ == "__main__":
    application()