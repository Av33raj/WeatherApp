#Api = 605da1fad476c6145be82d5f5a8f0ad2


import sys
import requests 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_lable = QLabel("Enter City name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton('Get weather', self)          # this section creats the lables and the emojis
        self.get_temp_lable = QLabel('70oF', self)                          # as well as the boxes on the GUI
        self.emo_lable = QLabel('🌞', self)
        self.desc_lable = QLabel('sunny ', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle ("Weather app")

        vBox = QVBoxLayout()

        vBox.addWidget(self.city_lable)
        vBox.addWidget(self.city_input)
        vBox.addWidget(self.get_weather_button)
        vBox.addWidget(self.get_temp_lable)
        vBox.addWidget(self.emo_lable)
        vBox.addWidget(self.desc_lable)

        self.setLayout(vBox)

        self.city_lable.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.get_temp_lable.setAlignment(Qt.AlignCenter)        # this centres all the code so its int the middle of the GIU
        self.emo_lable.setAlignment(Qt.AlignCenter)        
        self.desc_lable.setAlignment(Qt.AlignCenter)

        self.city_lable.setObjectName("City_lable")
        self.city_input.setObjectName("City_input")
        self.get_temp_lable.setObjectName("get_temp_lable")
        self.emo_lable.setObjectName("emo_lable")
        self.desc_lable.setObjectName("desc_lable")
        self.get_temp_lable.setObjectName("get_temp_lable")        

if __name__ =="__main__":               #This section will make the GUI application appear and so that
    app = QApplication(sys.argv)        #and it will stay till is interacted with 
    Weather_app = WeatherApp()
    Weather_app.show()          
    sys.exit(app.exec_())           

