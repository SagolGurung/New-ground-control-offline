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

        layout2 = QVBoxLayout(self.ui.cd2)

        self.layout3 = QVBoxLayout(self.ui.map)

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

        #FOR MODEL
        self.webview = QWebEngineView()

        # Load the desired website
        self.webview.load(QUrl("http://127.0.0.1:5500/modelshow.html"))

        
       
        #for map
        self.map = folium.Map(
                tiles='Stamen Terrain',
                name='real',
                zoom_start=12.5,
                max_zoom=21,
                attr='Google Map',

                location = (latitude,longitude) #coordinate replace with longitude and latitude latitude
            )
        self.map2 = folium.Map(
                tiles='Stamen Terrain',
                name='real',
                zoom_start=12.5,
                max_zoom=21,
                attr='Google Map',

                location = (latitude,longitude) #coordinate replace with longitude and latitude latitude
            )
        # self.marker1 = folium.Marker(
        # [27.717245,85.323959], popup="rocket", draggable= True
        # ).add_to(self.map) #marker1


    

        self.marker2 = folium.Marker(
        [27.6588, 85.3247], popup="rocketfinal"
        ).add_to(self.map)  # marker2

        self.line1 = 27.717245
        self.line2 = 85.323959

        folium.PolyLine([(27.717245, 85.323959),(27.6588, 85.3247)], weight = 18 , color = "yellow").add_to(self.map)

        folium.PolyLine([(27.717245, 85.323959), (27.6588, 85.3247)], fill=True, weight=2, fill_color="yellow",
                    color="red").add_to(self.map)
        
        
        layout2.addWidget(self.webview)
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
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(2000)

        #for map
        self.ui.start.clicked.connect(self.noshowmap)
        self.ui.start.clicked.connect(self.showmap)
        self.showmap()
        
        self.layout.addWidget(self.map_view)
    
        
    def noshowmap(self):
       
      
   
        self.ui.map.hide()  
        self.layout3.addWidget(self.map_view)

     
        
        
    def showmap(self):
                  #save map data to data object and layout
        
        self.i += 1 
        self.marker1 = folium.Marker(
        [self.line1, self.line2], popup="rocket", draggable= True, icon= folium.Icon(color='red')
        ).add_to(self.map) #marker1
        
        self.data = io.BytesIO()
        self.map.save(self.data, close_file=False)
        
        self.map_view = QWebEngineView()
       
        self.map_view.setHtml(self.data.getvalue().decode())
      
        self.layout.addWidget(self.map_view)
        
        
        self.ui.map.show()
           # Calculate the step size for the animation
        

        if self.i >= 1 and self.i <= 10:
            self.step_lat = (27.6588 -  27.717245) / 10
            self.step_lon = (85.3247 - 85.323959) / 10
            self.line1 += self.step_lat
            self.line2 += self.step_lon
 
      
 
    def update(self):
        

        self.line1 
        
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
        self.close()
      

        




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = mainmap()
    widget.show()
    app.exec_()