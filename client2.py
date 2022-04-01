import webbrowser
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox)

import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
    
        self.label1 = QLabel("Enter your hostname:", self)
        self.text1 = QLineEdit(self)
        self.text1.move(10, 30)

        self.label2 = QLabel("Enter your ip:", self)
        self.text2 = QLineEdit(self)
        self.text2.move(10, 120)
        self.label2.move(10, 100)

        self.label3 = QLabel("Enter your Api_key:", self)
        self.label3.move(10, 180)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 200)

        self.label4 = QLabel("Answer:", self)
        self.label4.move(10, 230)
        self.button = QPushButton("Send", self)
        self.button.move(10, 260)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text1.text()
        ip = self.text2.text()
        Api_key = self.text3.text()

        if ip == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname,ip, Api_key)
            if res:
    
                self.label4.setText("\n \n Longitude: %s \n Latitude: %s \n" % (res["Longitude"], res["Latitude"]))

                self.label4.adjustSize()

                self.show()

                url2 = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (res["Latitude"], res["Longitude"])

                webbrowser.open_new_tab(url2)


        
    def __query(self, hostname,ip, Api_key):
        url = "http://%s/ip/%s?key=%s" % (hostname,ip,Api_key)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()