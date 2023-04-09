import serial
import check
from check import update_gps_data

ser = serial.Serial('COM5', 115200) # Replace 'COM1' with the name of your serial port

data_array = [] # create an empty array to store the data


def datareader():

    i = 0
    while True:
        data = ser.readline().strip() # read data from the serial port and strip newline characters
        data_str = data.decode('utf-8') # convert byte string to regular string
        data_array.append(data_str) # add the data to the array
        
        # print('[{}]'.format(', '.join(data_array)))
        
        if len(data_array) >= i+4 :# check if there are enough elements in the array to read latitude and longitude
            latitude = data_array[i] 
            longitude = data_array[i+1]
            temperature = data_array[i+2]
            angle = data_array[i+3]
            # gps = data_array[i+4]
            check.update_gps_data(latitude,longitude,temperature,2000,angle,2,3,4)
            print('Latitude: {}, Longitude: {}, Temperature: {}'.format(latitude, longitude, temperature))

        
            i += 1 # increment the index variable by 2 to read the next set of values



    

datareader()