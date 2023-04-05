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
from final import Ui_finale #importing class from python file
from compass import Compass
from PyQt5.QtCore import QUrl
import serial.tools.list_ports
import time
import subprocess
from PyQt5.QtWebEngineWidgets import QWebEngineProfile
import json






class mainmap(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        self.i = 1

        super().__init__(*args, **kwargs)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.ui = Ui_finale()
        self.ui.setupUi(self)
        # self.uicompass = Compass()
        
        #--loads the map.ui 
        
        self.setWindowTitle("Ground control")

      
        
        
       
        #port initialization
        # ports = serial.tools.list_ports.comports()
        # self.serialInst = serial.Serial()
        # portlist = []
        # for onePort in ports:
        # 	portlist.append(str(onePort))
        # 	print (str(onePort))
        
        # self.serialInst.baudrate = 115200
        # self.serialInst.port = "COM26"
        # self.serialInst.open()

        #layout for model and map 
        self.layout = QVBoxLayout(self.ui.map)
        self.setLayout(self.layout)
        self.layout2 = QVBoxLayout(self.ui.map)

        # layoutcompass = QVBoxLayout(self.ui.compass)
        # self.setLayout(layoutcompass)
        
        #--gps datas
        #value_chain = com.getData()
        #big_data_array = calc.all_func()
        #print(big_data_array)
        #gps_array = big_data_array[6]

        latitude = 27.717245 #gps_array[0]
        longitude = 85.323959 #gps_array[1]

        #coordinate = (latitude[17], longitude[17])   

        # Load the desired website
        self.mapview = QWebEngineView(self)
        self.mapview.setGeometry(0, 0, 800, 600)
        profile = QWebEngineProfile.defaultProfile()
          # Start the HTTP server in a separate process
        
        self.http_server = subprocess.Popen(["python", "-m", "http.server", "8080"])
        
        profile.setHttpCacheType(QWebEngineProfile.NoCache)

        self.mapview.load(QUrl("http://127.0.0.1:8080/mapv3.html"))
        self.layout.addWidget(self.mapview)
        # layoutcompass.addWidget(self.uicompass)
    

        #button

        #self.clicked = [self.ui.coursebtn.clicked.connect(self.mode),self.ui.launch.clicked.connect(self.mode)]
        self.ui.cross.clicked.connect(self.close_window)


        #showing accurate direction
        # self.currentdirection =  self.uicompass.showdirection()

        # print(self.currentdirection)

        #slider  #inorder to show values from hardware , change the value of setValue = array[]
        self.ui.slideleft.valueChanged.connect(self.slidechange)
        # self.ui.slideleft.valueChanged.connect(self.noshowmap)
        # self.ui.slideleft.valueChanged.connect(self.showmap)

       
        
        self.ui.slideleft.setMaximum(50000)
        self.value = 0
        self.ui.slideleft.setValue(self.value)

        #slider2
        self.ui.slideright.valueChanged.connect(self.slidechange2)
       

        self.ui.slideright.setMaximum(50000)
        self.value2 = 0
        self.ui.slideleft.setValue(self.value2)

        #progressbar

        self.value4 = 10
        self.ui.battery.setValue(10)

        



    
        #creating timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.setInterval(2000)
        #creating timer 2
        self.timer2 = QTimer(self)
        self.timer2.setInterval(9000)
        self.timer2.timeout.connect(self.update2)
        self.ui.start.clicked.connect(self.update_angle)
        self.timer.start()
        self.timer2.start()

        

   
  
    
  


    def update2(self):
        # Use JavaScript to refresh the content of the page
        script = """
            var container = document.getElementById('map');
            var content = container.innerHTML;
            container.innerHTML = content;
        """
        self.mapview.page().runJavaScript(script, Qt.QueuedConnection)
        self.mapview.reload()



    def update(self):
        

     
        
        self.value += 100
        self.value2 += 100
        self.value4 += 1
        self.value3 = self.value+self.value2
        self.ui.slideleft.setValue(self.value)
        self.ui.slideright.setValue(self.value2)
        self.ui.speed1.setText(str(self.value3))
        self.ui.battery.setValue(self.value4)
        
        # self.ui.d3_value.setText(str())


        # packet = self.serialInst.readline()
        
        # data = packet.decode("utf").rstrip('\n')
        # self.ui.d3_value.setText(str(data))


  

    def update_angle(angle):
        # Load the JSON file
        with open('jsontest.json', 'r') as f:
            json_data = json.load(f)

        # Update the angle value in the JSON data
        json_data['angle'] = 90

        # Write the updated JSON data back to the file
        with open('jsontest.json', 'w') as f:
            json.dump(json_data, f)

    
    def refresh_page(self):
        self.mapview.reload()

    def portinitiate(self):
        

        return data

        # self.ui.d3_value.setText(str(data))

        
        
    def slidechange(self):
        
        self.value = self.ui.slideleft.value()
        self.ui.ovl4.setText(str(self.value))
    
    
    def slidechange2(self):
        self.value2 = self.ui.slideright.value()
        self.ui.ov1.setText(str(self.value2))

    # def getrawdata(self):
    # 	ser = serial.Serial('COM26', 115200, timeout=5)
    # 	data = b''
    # 	while True:
    # 		# read all available bytes from the serial port
    # 		new_data = ser.read(ser.in_waiting)
    # 		if not new_data:
    # 			break
    # 		data += new_data
    # 	# decode the accumulated data to a string
    # 	return data.decode()




    def mode(self):
    
    
        if self.clicked[0]:

            self.ui.direction1.setText("north")
            print("course")

        elif self.clicked == self.clicked[1]:
            self.ui.mode1.setText("launch")
            print("launch")


    
    
        
    def close_window(self):
        self.http_server.terminate()

        self.close()
      

        




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = mainmap()
    widget.show()
    app.exec_()