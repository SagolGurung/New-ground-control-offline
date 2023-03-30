import io

import folium
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.uic import loadUi
from jinja2 import Template
import calculation
import communication
import zoomed_map

com = communication.Communication()
calc = calculation.Calculation()
z = 0
zo = 0
maxAlt = 0
maxTemp = 0
maxPress = 0
maxAcc = 0
runtime_min, runtime_sec, runtime_hr = 0, 0, 0
seconday_map_window = 0

DEFAULT_STYLE1 = """QFrame{ border-radius:55px; background-color:qconicalgradient(cx:0.5, cy:0.5, 
           angle:90.0, stop:0 rgba(5, 3, 65, 255), stop:{STOP_1} rgba(5, 3, 65, 255), stop:{STOP_2} rgba(0, 0, 0, 
           0));} """

class Main_UI(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        loadUi("UI_V3.ui", self)
        # value_chain = com.getData()
        self.textBrowser.setTextColor(QColor(255, 255, 255))
        self.system_check.setStyleSheet(DEFAULT_STYLE)
        self.ignition.setStyleSheet(DEFAULT_STYLE)
        self.liftoff.setStyleSheet(DEFAULT_STYLE)   
        self.stage_seperation.setStyleSheet(DEFAULT_STYLE)
        self.rcs_fire.setStyleSheet(DEFAULT_STYLE)
        self.system_all_good.setStyleSheet(DEFAULT_STYLE)
        self.launch_success.setStyleSheet(DEFAULT_STYLE)
        layout = QVBoxLayout(self.frame)
        self.setLayout(layout)
        #big_data_array = calc.all_func()
        #gps_value = big_data_array[6]
        gps_value_latitude = gps_value[0]
        gps_value_longitude = gps_value[1]
        coordinate = (gps_value_latitude[17], gps_value_longitude[17])
        self.map = folium.Map(
            tiles='http://mt1.google.com/vt/lyrs=s&h1=p1Z&x={x}&y={y}&z={z}',
            name='real',
            zoom_start=19,
            attr='Google Map',
            location=coordinate,
            zoom_control=False,
            scrollWheelZoom=False,
            dragging=False
        )
        # folium.raster_layers.TileLayer(
        #     tiles='http://mt1.google.com/vt/lyrs=m&h1=p1Z&x={x}&y={y}&z={z}',
        #     name='Standard ',
        #     attr='Google Map',
        # ).add_to(self.map)
        #
        # folium.raster_layers.TileLayer(
        #     tiles='http://mt1.google.com/vt/lyrs=y&h1=p1Z&x={x}&y={y}&z={z}',
        #     name='Combined',
        #     attr='Google Map',
        # ).add_to(self.map)
        # folium.LayerControl().add_to(self.map)

        # save map data to data object
        data = io.BytesIO()
        folium.Marker(
            location=[gps_value_latitude[17], gps_value_longitude[17]],
                   ).add_to(self.map)
        self.map.save(data, close_file=False)
        self.map_view = QWebEngineView()
        self.map_view.setHtml(data.getvalue().decode())
        layout.addWidget(self.map_view)
        self.function()
        self.plot_thread()

    def plot_matplot(self):
        global z, seconday_map_window, altitude_value, maxAlt, maxTemp, maxPress, maxAcc
        big_data_array = calc.all_func()
        print(big_data_array)
        altitude_array = big_data_array[0]
        temperature_array = big_data_array[1]
        pressure_array = big_data_array[2]
        acceleration_array = big_data_array[3]
        gyroscope_array = big_data_array[4]
        vibration_array = big_data_array[5]
        gps_value = big_data_array[6]
        pointer = altitude_array[0]
        self.run_time()
        if seconday_map_window == 0:  # donot run primary window if zoomed_map is open
            self.mplWidget.canvas.ax1.cla()
            self.mplWidget.canvas.ax1.grid(color='w', linestyle='-', linewidth=0.1)
            self.mplWidget.canvas.ax1.plot(pointer, altitude_array[1], c="orange")
            self.mplWidget.canvas.ax1.plot(pointer, altitude_array[2], c="blue")
            self.altitude_lcd.display(altitude_array[1][17])
            self.Pointer_lcd.display(altitude_array[0][17])
            test = altitude_array[1][17]
            if test > maxAlt:
                self.Max_Altitude.display(test)
                maxAlt = test
            else:
                self.Max_Altitude.display(maxAlt)
            if altitude_array[1][17] > 250:
                self.system_check.setStyleSheet(COMPLETED_STYLE)
            elif altitude_array[1][17] >= 200:
                self.system_check.setStyleSheet(NOTGOOD_STYLE)

            self.mplWidget.canvas.ax2.cla()
            self.mplWidget.canvas.ax2.grid(color='w', linestyle='-', linewidth=0.1)
            self.mplWidget.canvas.ax2.plot(pointer, vibration_array[0], c="green")  # upper only

            self.mplWidget.canvas.ax3.cla()
            self.mplWidget.canvas.ax3.grid(color='w', linestyle='-', linewidth=0.1)
            self.mplWidget.canvas.ax3.plot(pointer, temperature_array[0], c="orange")  # upper only
            self.Temperature_lcd.display(temperature_array[0][17])
            test = temperature_array[0][17]
            if test > maxTemp:
                self.Max_Temperature.display(test)
                maxTemp = test
            else:
                self.Max_Temperature.display(maxTemp)
            self.mplWidget.canvas.ax4.cla()
            self.mplWidget.canvas.ax4.grid(color='w', linestyle='-', linewidth=0.1)
            self.mplWidget.canvas.ax4.plot(pointer, pressure_array[0], c="yellow")
            test =  pressure_array[0][17]
            if test > maxPress:
                self.Max_Pressure.display(test)
                maxPress = test
            else:
                self.Max_Pressure.display(maxPress)

            self.mplWidget.canvas.ax5.cla()
            self.mplWidget.canvas.ax5.grid(color='w', linestyle='-', linewidth=0.1)
            self.mplWidget.canvas.ax5.plot(pointer, acceleration_array[0])  # upper only x
            self.mplWidget.canvas.ax5.plot(pointer, acceleration_array[1])  # y
            self.mplWidget.canvas.ax5.plot(pointer, acceleration_array[2])  # z
            test = acceleration_array[2][17]
            if test > maxAcc:
                self.Max_Acceleration.display(test)
                maxAcc = test
            else:
                self.Max_Acceleration.display(maxAcc)
            self.mplWidget.canvas.ax6.cla()
            self.mplWidget.canvas.ax6.grid(color='w', linestyle='-', linewidth=0.1)
            self.mplWidget.canvas.ax6.plot(pointer, gyroscope_array[0])  # upper only x
            self.mplWidget.canvas.ax6.plot(pointer, gyroscope_array[1])  # y
            self.mplWidget.canvas.ax6.plot(pointer, gyroscope_array[2])  # z

            self.mplWidget.canvas.ax_3d.cla()
            self.mplWidget.canvas.ax2.grid(color='w', linestyle='-', linewidth=0.1)
            self.mplWidget.canvas.ax_3d.scatter(gps_value[0], gps_value[1], altitude_array[1],
                                                c="black")
            self.latitude_lcd.display('{:.02f}'.format(gps_value[0][17]))
            self.longitude_lcd.display('{:.02f}'.format(gps_value[1][17]))
            self.mplWidget.canvas.draw()
            self.add_marker(gps_value)
            self.textBrowser.append(str(gps_value))

            # flight status meaning ignition , liftoff or any other state
            self.textBrowser_2.append(str("Latest flight status is shown here"))
            self.textBrowser_2.append(str(z))
            temperature_progress = altitude_array[0]
            progress = (100 - temperature_progress[17]) / 100.0
            print(progress)
            STOP_1 = str(progress)
            STOP_2 = str(progress)
            if progress < 0:
                progress = 0
            styleSheet = DEFAULT_STYLE1.replace("{STOP_1}", str(progress - 0.001)).replace("{STOP_2}", str(progress))
            self.temperature_visual.setStyleSheet(styleSheet)
            self.textBrowser.verticalScrollBar().maximum()
            temperature_progress = temperature_array[0]
            progress = (100 - temperature_progress[17]) / 100.0
            # print(progress)
            STOP_1 = str(progress)
            STOP_2 = str(progress)
            if progress < 0:
                progress = 0
            styleSheet_1 = DEFAULT_STYLE1.replace("{STOP_1}", str(progress - 0.001)).replace("{STOP_2}", str(progress))
            self.temperature_visual_1.setStyleSheet(styleSheet_1)

        else:
            return gps_value

    def plot_thread(self):
        self.plot_matplot()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.plot_matplot)
        self.timer.start()

    def add_marker(self, value_chainU):
        global z, gps_value_latitude, gps_value_longitude
        gps_value_latitude = value_chainU[0]
        gps_value_longitude = value_chainU[1]
        global z
        z = z + 1
        if z == 0:
            js = Template(
                """
            L.circleMarker(
                [{{latitude}}, {{longitude}}], {
                    "bubblingMouseEvents": true,
                    "color": "red",
                    "dashArray": null,
                    "dashOffset": null,
                    "fill": false,
                    "fillColor": "#3388ff",
                    "fillOpacity": 0.2,
                    "fillRule": "evenodd",
                    "lineCap": "round",
                    "lineJoin": "round",
                    "opacity": 1.0,
                    "radius": 0.1,
                    "stroke": true,
                    "weight": 5
                }
            ).addTo({{map}});
            """
            ).render(map=self.map.get_name(), latitude=gps_value_latitude[17], longitude=gps_value_longitude[17])
            self.map_view.page().runJavaScript(js)

        if z == 1:
            js = Template(
                """
            L.circleMarker(
                [{{latitude}}, {{longitude}}], {
                    "bubblingMouseEvents": true,
                    "color": "yellow",
                    "dashArray": null,
                    "dashOffset": null,
                    "fill": false,
                    "fillColor": "#3388ff",
                    "fillOpacity": 0.2,
                    "fillRule": "evenodd",
                    "lineCap": "round",
                    "lineJoin": "round",
                    "opacity": 1.0,
                    "radius": 0.1,
                    "stroke": true,
                    "weight": 5
                }
            ).addTo({{map}});
            """
            ).render(map=self.map.get_name(), latitude=gps_value_latitude[17], longitude=gps_value_longitude[17])
            self.map_view.page().runJavaScript(js)
            z = -1

    def function(self):
        self.map_button.setStyleSheet("background-color : #005500")
        self.wifi.setStyleSheet("background-color : #005500")
        self.record_button.setStyleSheet("background-color :#a60000")
        self.gps_connection.setStyleSheet("background-color : #005500")
        self.minimize_button.clicked.connect(self.minimize_window)
        # self.maximize_button.clicked.connect(self.maximize_window)
        self.close_button.clicked.connect(self.close_window)
        self.map_button.clicked.connect(self.show_map_window)

    def show_map_window(self, checked):
        global seconday_map_window
        seconday_map_window = 1
        self.close()
        self.w = zoomed_map.Map_UI()
        self.w.show()
        self.close()

    def minimize_window(self):
        self.showMinimized()

    def close_window(self):
        global seconday_map_window
        seconday_map_window = 0
        QtCore.QCoreApplication.instance().quit()

    def run_time(self):
        global runtime_min, runtime_sec, runtime_hr
        runtime_sec = runtime_sec + 1
        self.second_lcd.display(runtime_sec)
        if runtime_sec == 59:
            runtime_sec = 0
            runtime_min = runtime_min + 1
            self.minute_lcd.display(runtime_min)
            if runtime_min == 59:
                runtime_min = 0
                runtime_hr = runtime_hr + 1
                self.hour_lcd.display(runtime_hr)


DEFAULT_STYLE = """
QProgressBar{
    background-color :rgb(0,0,0);
    border-radius: 10px;
}

QProgressBar::chunk {
    background : rgb(29, 185, 84);;
    width: 10px;
    margin: 1px;
}
"""

COMPLETED_STYLE = """
QProgressBar{
    background-color :rgb(29, 185, 84);
    border-radius: 10px;
}

QProgressBar::chunk {
    background : rgb(29, 185, 84);;
    width: 10px;
    margin: 1px;
}
"""

NOTGOOD_STYLE = """
QProgressBar{
    background-color :YELLOW;
    border-radius: 10px;
}

QProgressBar::chunk {
    background : rgb(29, 185, 84);;
    width: 10px;
    margin: 1px;
}
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Main_UI()
    window.show()
    app.exec_()
