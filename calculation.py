import tracemalloc
import numpy as np
from communication import Communication


value_chainD = [0] * 18
# Altitude values
altitude_dataU = np.linspace(0, 0, 18)
altitude_dataL = np.linspace(0, 0, 18)
ptr1 = 0
xa_data = np.linspace(0, 0, 18)
maxAlt = 0
ignition = 0
height_a = 0
# Acceleration values
acceleration_dataUx = np.linspace(0, 0, 18)
acceleration_dataLz = np.linspace(0, 0, 18)
acceleration_dataUy = np.linspace(0, 0, 18)
acceleration_dataUz = np.linspace(0, 0, 18)
xa4_data = np.linspace(0, 0, 18)
ptr5 = 0
maxAcc = 0
# Velocity values
velocity_dataU = np.linspace(0, 0, 18)
velocity_dataL = np.linspace(0, 0, 18)
xa1_data = np.linspace(0, 0, 18)
ptr2 = 0
maxVe = 0
# Temperature values
temperature_dataU = np.linspace(0, 0, 18)
temperature_dataL = np.linspace(0, 0, 18)
xa2_data = np.linspace(0, 0, 18)
ptr3 = 0
maxTemp = 0
# Pressure values
pressure_dataU = np.linspace(0, 0, 18)
pressure_dataL = np.linspace(0, 0, 18)
xa3_data = np.linspace(0, 0, 18)
ptr4 = 0
maxPress = 0
# Vibration values
vibration_dataU = np.linspace(0, 0, 18)
vibration_dataL = np.linspace(0, 0, 18)
xa6_data = np.linspace(0, 0, 18)
ptr7 = 0
# Gyroscope values
gyro_data_x = np.linspace(0, 0, 18)
gyro_data_y = np.linspace(0, 0, 18)
gyro_dataU_z = np.linspace(0, 0, 18)
gyro_dataL_z = np.linspace(0, 0, 18)
xa5_data = np.linspace(0, 0, 18)
ptr6 = 0
# other
val = Communication()
satellite_deployment = 0
drough_parachute = 0
main_parachute = 0
touch_down = 0
liftoff = 0
value_chainL = [0] * 18
value_chainU = [0] * 18

gps_data_lat = np.linspace(0, 0, 18)
gps_data_long = np.linspace(0, 0, 18)
map_update = 0
i = 0
z = -1
big_array = []
runtime_min, runtime_sec, runtime_hr = 0, 0, 0
tracemalloc.start()

class Calculation:
    global big_array

    def altitude_func(self, value_chainU, value_chainL):
        global altitude_dataU, altitude_dataL, ptr1, xa_data, maxAlt, ignition, height_a, drough_parachute, main_parachute, satellite_deployment
        altitude_dataU[:-1] = altitude_dataU[1:]
        altitude_dataU[-1] = float(value_chainU[1])
        altitude_dataL[:-1] = altitude_dataL[1:]
        altitude_dataL[-1] = float(value_chainL[1])
        ptr1 += 1
        xa_data[:-1] = xa_data[1:]
        xa_data[-1] = float(ptr1)
        return xa_data, altitude_dataU, altitude_dataL
        # print('altitude = ', altitude_dataU)
        # test = altitude_dataU[12]
        # if test > maxAlt:
        #     self.maxi_altitude.display(test)
        #     maxAlt = test
        # else:
        #     self.maxi_altitude.display(maxAlt)
        #
        # if acceleration_dataUz[12] > 0:
        #     ignition = 1
        #     self.ignition.setStyleSheet("QProgressBar"
        #                                 "{"
        #                                 "background-color : rgb(0, 0, 0);"
        #                                 "border : 1px"
        #                                 "}"
        #                                 "QProgressBar::chunk"
        #                                 "{"
        #                                 "background : rgb(29, 185, 84);"
        #                                 "}"
        #                                 )
        # elif ignition == 1:
        #     self.ignition.setStyleSheet("QProgressBar"
        #                                 "{"
        #                                 "background-color : rgb(0, 0, 0);"
        #                                 "border : 1px"
        #                                 "}"
        #                                 "QProgressBar::chunk"
        #                                 "{"
        #                                 "background : rgb(29, 185, 84);"
        #                                 "}"
        #                                 )
        # else:
        #     self.ignition.setStyleSheet("QProgressBar"
        #                                 "{"
        #                                 "background-color : rgb(0, 0, 0);"
        #                                 "border : 1px"
        #                                 "}"
        #                                 "QProgressBar::chunk"
        #                                 "{"
        #                                 "background : rgb(0, 0,0);"
        #                                 "}"
        #                                 )
        # if altitude_dataU[12] >= 6000:  # apogee at 6km
        #     height_a = 1
        #     self.Maxheight.setStyleSheet("QProgressBar"
        #                                  "{"
        #                                  "background-color : rgb(0, 0, 0);"
        #                                  "border : 1px"
        #                                  "}"
        #                                  "QProgressBar::chunk"
        #                                  "{"
        #                                  "background : rgb(29, 185, 84);"
        #                                  "}"
        #                                  )
        # elif height_a == 1:
        #     self.Maxheight.setStyleSheet("QProgressBar"
        #                                  "{"
        #                                  "background-color : rgb(0, 0, 0);"
        #                                  "border : 1px"
        #                                  "}"
        #                                  "QProgressBar::chunk"
        #                                  "{"
        #                                  "background : rgb(29, 185, 84);"
        #                                  "}"
        #                                  )
        #
        # else:
        #     self.Maxheight.setStyleSheet("QProgressBar"
        #                                  "{"
        #                                  "background-color : rgb(0, 0, 0);"
        #                                  "border : 1px"
        #                                  "}"
        #                                  "QProgressBar::chunk"
        #                                  "{"
        #                                  "background : rgb(0, 0,0);"
        #                                  "}"
        #                                  )
        # if value_chainU[13] == '1':
        #     satellite_deployment = 1
        #     self.payload.setStyleSheet("QProgressBar"
        #                                "{"
        #                                "background-color : rgb(0, 0, 0);"
        #                                "border : 1px"
        #                                "}"
        #                                "QProgressBar::chunk"
        #                                "{"
        #                                "background : rgb(0, 0,0);"
        #                                "}"
        #                                )
        # else:
        #     self.payload.setStyleSheet("QProgressBar"
        #                                "{"
        #                                "background-color : rgb(0, 0, 0);"
        #                                "border : 1px"
        #                                "}"
        #                                "QProgressBar::chunk"
        #                                "{"
        #                                "background : rgb(29, 185, 84);"
        #                                "}"
        #                                )
        # if int(value_chainU[14]) == 1:
        #     drough_parachute = 1
        #     self.drough.setStyleSheet("QProgressBar"
        #                               "{"
        #                               "background-color : rgb(0, 0, 0);"
        #                               "border : 1px"
        #                               "}"
        #                               "QProgressBar::chunk"
        #                               "{"
        #                               "background : rgb(29, 185, 84);"
        #                               "}"
        #                               )
        # else:
        #     self.drough.setStyleSheet("QProgressBar"
        #                               "{"
        #                               "background-color : rgb(0, 0, 0);"
        #                               "border : 1px"
        #                               "}"
        #                               "QProgressBar::chunk"
        #                               "{"
        #                               "background : rgb(0,0,0);"
        #                               "}"
        #                               )
        # if int(value_chainU[15]) == 1:
        #     main_parachute = 1
        #     self.main_parachute.setStyleSheet("QProgressBar"
        #                                       "{"
        #                                       "background-color : rgb(0, 0, 0);"
        #                                       "border : 1px"
        #                                       "}"
        #                                       "QProgressBar::chunk"
        #                                       "{"
        #                                       "background : rgb(29, 185, 84);"
        #                                       "}"
        #                                       )
        # else:
        #     self.main_parachute.setStyleSheet("QProgressBar"
        #                                       "{"
        #                                       "background-color : rgb(0, 0, 0);"
        #                                       "border : 1px"
        #                                       "}"
        #                                       "QProgressBar::chunk"
        #                                       "{"
        #                                       "background : rgb(0, 0,0);"
        #                                       "}"
        #                                       )
        # if int(value_chainU[1]) >= 1248:
        #     self.landing.setStyleSheet("QProgressBar"
        #                                "{"
        #                                "background-color : rgb(0, 0, 0);"
        #                                "border : 1px"
        #                                "}"
        #                                "QProgressBar::chunk"
        #                                "{"
        #                                "background : rgb(185,185,0);"
        #                                "}"
        #                                )
        #     if ignition == 1 and liftoff == 1:
        #         self.landing.setStyleSheet("QProgressBar"
        #                                    "{"
        #                                    "background-color : rgb(0, 0, 0);"
        #                                    "border : 1px"
        #                                    "}"
        #                                    "QProgressBar::chunk"
        #                                    "{"
        #                                    "background : rgb(135,185,0);"
        #                                    "}"
        #                                    )
        #         if satellite_deployment == 1 and drough_parachute == 1:
        #             self.landing.setStyleSheet("QProgressBar"
        #                                        "{"
        #                                        "background-color : rgb(0, 0, 0);"
        #                                        "border : 1px"
        #                                        "}"
        #                                        "QProgressBar::chunk"
        #                                        "{"
        #                                        "background : rgb(85,185,0);"
        #                                        "}"
        #                                        )
        #             if main_parachute == 1 and touch_down == 1:
        #                 self.landing.setStyleSheet("QProgressBar"
        #                                            "{"
        #                                            "background-color : rgb(0, 0, 0);"
        #                                            "border : 1px"
        #                                            "}"
        #                                            "QProgressBar::chunk"
        #                                            "{"
        #                                            "background : rgb(29, 185, 84);"
        #                                            "}"
        #                                            )
        #
        #     else:
        #         self.landing.setStyleSheet("QProgressBar"
        #                                    "{"
        #                                    "background-color : rgb(0, 0, 0);"
        #                                    "border : 1px"
        #                                    "}"
        #                                    "QProgressBar::chunk"
        #                                    "{"
        #                                    "background : rgb(0, 0,0);"
        #                                    "}"
        #                                    )
        #
        #     self.launch_success.setStyleSheet("QProgressBar"
        #                                       "{"
        #                                       "background-color : rgb(0, 0, 0);"
        #                                       "border : 1px"
        #                                       "}"
        #                                       "QProgressBar::chunk"
        #                                       "{"
        #                                       "background : rgb(5, 0,0);"
        #                                       "}"
        #                                       )

    # def velocity_func(self, value_chainU, value_chainL):
    #     global velocity_dataU, velocity_dataL, ptr2, xa1_data, maxVe
    #     velocity_dataU[:-1] = velocity_dataU[1:]
    #     velocity_dataU[-1] = float(value_chainU[3])
    #     velocity_dataL[:-1] = velocity_dataL[1:]
    #     velocity_dataL[-1] = float(value_chainL[3])
    #     ptr2 += 1
    #     xa1_data[:-1] = xa1_data[1:]
    #     xa1_data[-1] = float(ptr2)
    #     return velocity_dataU, velocity_dataL
    #     # print('velocity =', velocity_data)
    #     #
    #     # test = velocity_dataU[12]
    #     # if test > maxVe:
    #     #     self.maxi_velocity.display(test)
    #     #     maxVe = test
    #     # else:
    #     #     self.maxi_velocity.display(maxVe)

    #def temp_func(self, value_chainU, value_chainL):
        global temperature_dataU, temperature_dataL, ptr3, xa2_data, maxTemp
        temperature_dataU[:-1] = temperature_dataU[1:]
        temperature_dataU[-1] = float(value_chainU[11])
        temperature_dataL[:-1] = temperature_dataL[1:]
        temperature_dataL[-1] = float(value_chainL[11])
        ptr3 += 1
        xa2_data[:-1] = xa2_data[1:]
        xa2_data[-1] = float(ptr3)
        return temperature_dataU, temperature_dataL
        # print('temperature =', temperature_data)
        # test = temperature_dataU[12]
        # if test > maxTemp:
        #     self.maxi_temp.display(test)
        #     maxTemp = test
        # else:
        #     self.maxi_temp.display(maxTemp)

    #def press_func(self, value_chainU, value_chainL):
        global pressure_dataU, pressure_dataL, ptr4, xa3_data, maxPress
        pressure_dataU[:-1] = pressure_dataU[1:]
        pressure_dataU[-1] = float(value_chainU[10])  # find position in value chain
        pressure_dataL[:-1] = pressure_dataL[1:]
        pressure_dataL[-1] = float(value_chainL[10])
        ptr4 += 1
        xa3_data[:-1] = xa3_data[1:]
        xa3_data[-1] = float(ptr4)
        return pressure_dataU, pressure_dataL
        # print('pressure =', pressure_data)
        # test = pressure_dataU[12]
        # if test > maxPress:
        #     self.maxi_pressure.display(test)
        #     maxPress = test
        # else:
        #     self.maxi_pressure.display(maxPress)

    #def acc_func(self, value_chainU, value_chainL):
        global acceleration_dataUx, acceleration_dataUy, acceleration_dataUz, acceleration_dataLz, ptr5, xa4_data, maxAcc, liftoff

        acceleration_dataUx[:-1] = acceleration_dataUx[1:]
        acceleration_dataUx[-1] = float(value_chainU[3])
        acceleration_dataUy[:-1] = acceleration_dataUy[1:]
        acceleration_dataUy[-1] = float(value_chainU[4])
        acceleration_dataUz[:-1] = acceleration_dataUz[1:]
        acceleration_dataUz[-1] = float(value_chainU[5])
        acceleration_dataLz[:-1] = acceleration_dataLz[1:]
        acceleration_dataLz[-1] = float(value_chainL[5])
        ptr5 += 1
        xa4_data[:-1] = xa4_data[1:]
        xa4_data[-1] = float(ptr5)
        return acceleration_dataUx, acceleration_dataUy, acceleration_dataUz, acceleration_dataLz
        # print(acceleration_dataLz)

        # print(value_chain)
        # test = acceleration_dataUz[12]
        #
        # if test > maxAcc:
        #     gforce = test / 9.8
        #     self.maxi_acc.display(gforce)
        #     maxAcc = test
        # else:
        #     gforce = maxAcc / 9.8
        #     self.maxi_acc.display(gforce)
        #
        # if ignition >= 1:
        #     if acceleration_dataUz[12] > 10:
        #         liftoff += 1
        #         self.Liftoff.setStyleSheet("QProgressBar"
        #                                    "{"
        #                                    "background-color : rgb(0, 0, 0);"
        #                                    "border : 1px"
        #                                    "}"
        #                                    "QProgressBar::chunk"
        #                                    "{"
        #                                    "background : rgb(29, 185, 84);"
        #                                    "}"
        #                                    )
        # elif liftoff >= 1:
        #     self.Liftoff.setStyleSheet("QProgressBar"
        #                                "{"
        #                                "background-color : rgb(0, 0, 0);"
        #                                "border : 1px"
        #                                "}"
        #                                "QProgressBar::chunk"
        #                                "{"
        #                                "background : rgb(29, 185, 84);"
        #                                "}"
        #                                )
        # else:
        #     self.Liftoff.setStyleSheet("QProgressBar"
        #                                "{"
        #                                "background-color : rgb(0, 0, 0);"
        #                                "border : 1px"
        #                                "}"
        #                                "QProgressBar::chunk"
        #                                "{"
        #                                "background : rgb(0, 0, 0);"
        #                                "}"
        #                                )

    #def gyro_func(self, value_chainU, value_chainL):

        global gyro_data_x, gyro_data_y, gyro_dataU_z, gyro_dataL_z, ptr6, xa5_data

        gyro_data_x[:-1] = gyro_data_x[1:]
        gyro_data_x[-1] = float(value_chainU[5])
        gyro_data_y[:-1] = gyro_data_y[1:]
        gyro_data_y[-1] = float(value_chainU[6])
        gyro_dataU_z[:-1] = gyro_dataU_z[1:]
        gyro_dataU_z[-1] = float(value_chainU[7])
        gyro_dataL_z[:-1] = gyro_dataL_z[1:]
        gyro_dataL_z[-1] = float(value_chainL[5])
        ptr6 += 1
        xa5_data[:-1] = xa5_data[1:]
        xa5_data[-1] = float(ptr6)
        return gyro_data_x, gyro_data_y, gyro_dataU_z, gyro_dataL_z

    #def vibration_func(self, value_chainU, value_chainL):
        global vibration_dataU, vibration_dataL, ptr7, xa6_data, map_update
        vibration_dataU[:-1] = vibration_dataU[1:]
        vibration_dataU[-1] = float(value_chainU[6])
        vibration_dataL[:-1] = vibration_dataL[1:]
        vibration_dataL[-1] = float(value_chainL[6])
        ptr7 += 1
        xa6_data[:-1] = xa6_data[1:]
        xa6_data[-1] = float(ptr7)
        return vibration_dataU, vibration_dataL
        # if value_chainU == 0.00:
        #     self.GPS_status.setStyleSheet("QProgressBar"
        #                                   "{"
        #                                   "background-color : rgb(0, 0, 0);"
        #                                   "border : 1px"
        #                                   "}"
        #
        #                                   "QProgressBar::chunk"
        #                                   "{"
        #                                   "background : rgb(255, 0,0);"
        #                                   "}"
        #                                   )
        # else:
        #     self.GPS_status.setStyleSheet("QProgressBar"
        #                                   "{"
        #                                   "background-color : rgb(0, 0, 0);"
        #                                   "border : 1px"
        #                                   "}"
        #
        #                                   "QProgressBar::chunk"
        #                                   "{"
        #                                   "background : rgb(100, 50,0);"
        #                                   "}"
        #                                   )

    def progress_bar(self, value_chainU, value_chainL):
        if int(value_chainU[1]) == 1294:  # SET VALUE
            self.ignition.setStyleSheet("QProgressBar"
                                        "{"
                                        "background-color : rgb(0, 0, 0);"
                                        "border : 1px"
                                        "}"

                                        "QProgressBar::chunk"
                                        "{"
                                        "background : rgb(100, 50,0);"
                                        "}"
                                        )
        else:
            self.ignition.setStyleSheet("QProgressBar"
                                        "{"
                                        "background-color : rgb(0, 0, 0);"
                                        "border : 1px"
                                        "}"

                                        "QProgressBar::chunk"
                                        "{"
                                        "background : rgb(0, 0,0);"
                                        "}"
                                        )

        self.Maxheight.setStyleSheet("QProgressBar"
                                     "{"
                                     "background-color : rgb(0, 0, 0);"
                                     "border : 1px"
                                     "}"
                                     "QProgressBar::chunk"
                                     "{"
                                     "background : rgb(0, 0,0);"
                                     "}"
                                     )



    def update_graph(self):
        value_chain = val.getData()
        value_chainL = value_chain  # change it while testing
        value_chainU = value_chain
        gps_data_lat[:-1] = gps_data_lat[1:]
        gps_data_lat[-1] = float(value_chainU[8])
        gps_data_long[:-1] = gps_data_long[1:]
        gps_data_long[-1] = float(value_chainL[9])

    def all_func(self):
        global gps_array
        value_chain = val.getData()
        # print('from main', value_chainU)
        value_chainL = value_chain[0]  # change it while testing
        value_chainU = value_chain[0] # change it while testing
        # ###############################turn it on for actual testing###################
        # if value_chain[0] == 'L':
        #     value_chainL = value_chain
        #     # print('from main', value_chainL)
        # elif value_chain[0] == 'U':
        #     value_chainU = value_chain
        #     print('from main', value_chainU)
        #
        # if len(value_chain) <= 18:
        #     value_chainL = value_chainU
        # if value_chain[0] != 'L' and value_chain[0] != 'U':
        #     gps_array = value_chain
        gps_array = value_chain[1]
        big_array.clear()
        #big_array.append(self.altitude_func(value_chainU, value_chainL))
        # big_array.append(self.vibration_func(value_chainU, value_chainL))
        #big_array.append(self.temp_func(value_chainU, value_chainL))
        #big_array.append(self.press_func(value_chainU, value_chainL))
        #big_array.append(self.acc_func(value_chainU, value_chainL))
        #big_array.append(self.gyro_func(value_chainU, value_chainL))
        #big_array.append(self.vibration_func(value_chainU, value_chainL))
        big_array.append(gps_array)
        print(big_array)
        return big_array
        # self.progress_bar(value_chainU, value_chainL)
        # self.add_marker(value_chainU, value_chainL)
        # self.run_time()
        # data_base.guardar(value_chain)
if __name__=="__main__":
    great = Calculation()
    great.all_func()
