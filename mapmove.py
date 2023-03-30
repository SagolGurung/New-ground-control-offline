import folium
import time

class Map:
    def __init__(self):
        self.map = folium.Map(location=[27.717245, 85.323959], zoom_start=13)

        # create the yellow polyline
        self.yellow_polyline = folium.PolyLine([(27.6588, 85.3247), (27.717245, 85.323959)], weight=18, color="yellow")
        self.yellow_polyline.add_to(self.map)

        # create the red polyline
        self.red_polyline = folium.PolyLine([(27.717245, 85.323959), (27.6588, 85.3247)], fill=True, weight=2, fill_color="yellow", color="red")
        self.red_polyline.add_to(self.map)

    def animate(self, destination):
        # update the location of the yellow polyline in a loop
        while True:
            # calculate the direction of movement
            delta_lat = (destination[0] - self.yellow_polyline.locations[-1][0]) / 50
            delta_lon = (destination[1] - self.yellow_polyline.locations[-1][1]) / 50

            # update the location of the yellow polyline
            locations = self.yellow_polyline.locations
            locations.append((locations[-1][0] + delta_lat, locations[-1][1] + delta_lon))
            self.yellow_polyline.locations = locations

            # redraw the map
            self.map.add_children(self.yellow_polyline)
            time.sleep(0.1)
# create the map object
m = Map()

# animate the yellow polyline to a new destination
m.animate([27.6788, 85.3147])