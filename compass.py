from PyQt5.QtCore import QPoint, Qt, QTimer
from PyQt5.QtGui import QColor, QPainter, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets   
import serial.tools.list_ports
import serial


class Compass(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        self.setGeometry(140, 120, 180, 180)
        

       
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(50)

        ports = serial.tools.list_ports.comports()
        self.serialInst = serial.Serial()
        portlist = []
        for onePort in ports:
                portlist.append(str(onePort))
                print (str(onePort))
            
        self.serialInst.baudrate = 115200
        self.serialInst.timeout = 5
        self.serialInst.port = "COM26"
        self.serialInst.open()


    

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        
        painter = QPainter(self)
        
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(100,100)
        painter.scale(side / 100, side / 100)
        painter.setPen(Qt.NoPen)


        # Draw the compass needle
        painter.setBrush(Qt.green)
        painter.save()

        #headig to return the value
        try:
                
            heading = self.get_heading()
            painter.rotate(heading)
            painter.drawConvexPolygon(QPolygon([QPoint(0, -50), QPoint(5, 0), QPoint(-5, 0)]))
            painter.restore()
        
        except TypeError:
            pass
        
       

    def get_heading(self):

        try:

            packet = self.serialInst.readline()
            data = packet.decode("utf").rstrip('\n')
            self.final_data = float(data)

            self.final_data += 0

            if self.final_data >=362:
                self.data = 0
        
            

            return self.final_data

        except UnicodeDecodeError:
        # Handle the exception
            pass

        
    



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    compass = Compass()
    compass.show()
   
    sys.exit(app.exec_())