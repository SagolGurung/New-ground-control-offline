import io
from jinja2 import Template
import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets    
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import QPoint, Qt, QTimer
from PyQt5.QtGui import QColor, QPainter, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
#import main
from PyQt5.QtWidgets import QVBoxLayout
from new import Ui_Main_UI #importing class from python file
from PyQt5.QtCore import QUrl



class mainw(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Main_UI()
        self.ui.setupUi(self)
        self.setWindowTitle("Ground control main")

        layout = QVBoxLayout(self.ui.frame)

        #FOR MODEL
        self.webview = QWebEngineView()

        # Load the desired website
        self.webview.load(QUrl("http://127.0.0.1:5500/orientedshape.html"))
        layout.addWidget(self.webview)
       

        self.ui.close_button.clicked.connect(self.close_window)

    def close_window(self):
        self.close()


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    widget = mainw()
    widget.show()
    app.exec_()

