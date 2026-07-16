#Api = 605da1fad476c6145be82d5f5a8f0ad2


import sys
import requests 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()


if __name__ =="__main__":               #This section will make the GUI application appear and so that
    app = QApplication(sys.argv)        #and it will stay till is interacted with 
    Weather_app = WeatherApp()
    Weather_app.show()          
    sys.exit(app.exec_())           #

