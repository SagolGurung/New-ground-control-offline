import json

# Load the initial values from a JSON file
with open('jsontest.json') as f:
    data = json.load(f)
    jlatitude = data['latitude']
    jlongitude = data['longitude']

# Define the other variables
jtemperature = data['temperature']
jaltitude = data['altitude']
jangle = data['angle']
jorientationX = data['orientationX']
jorientationY = data['orientationY']
jorientationZ = data['orientationZ']

def update_gps_data(new_latitude, new_longitude, new_temperature, new_altitude, new_angle, new_orientationX, new_orientationY, new_orientationZ):
    # Update the global variables
    global jlatitude, jlongitude, jtemperature, jaltitude, jangle, jorientationX, jorientationY, jorientationZ
    jlatitude = new_latitude
    jlongitude = new_longitude
    jtemperature = new_temperature
    jaltitude = new_altitude
    jangle = new_angle
    jorientationX = new_orientationX
    jorientationY = new_orientationY
    jorientationZ = new_orientationZ

    # Save the updated GPS data to a JSON file
    gps_data = {
        'latitude': jlatitude,
        'longitude': jlongitude,
        'temperature': jtemperature,
        'altitude': jaltitude,
        'angle': jangle,
        'orientationX': jorientationX,
        'orientationY': jorientationY,
        'orientationZ': jorientationZ
    }
    with open('jsontest.json', 'w') as f:
        json.dump(gps_data, f)
