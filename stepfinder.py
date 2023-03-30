




class stepfinder():
    def __init__(self,longitude:float,latitude:float,longitude2:float,latitude2:float):
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.longitude2 = float(longitude2)
        self.latitude2 = float(latitude2)
        
   
    
    def stepcalc(self):
        

        self.step_lon = float((self.longitude2 - self.longitude)/ 20)
        self.step_lat =float((self.latitude2 - self.latitude)/20)
       
        self.longitudes = []
        self.latitudes = []
        i = 0
        self.yes_no = str(input('do you want it raw?y/n: '))
        while True:
           
            
            
            self.longitude += self.step_lon
            self.latitude += self.step_lat
            self.final = format(self.longitude,'.4f')
            self.final2 =format(self.latitude,'.4f')
            self.longitudes.append(self.final)
            self.latitudes.append(self.final2)

            if len(self.latitudes) > 5 and self.yes_no =='Y':
                
                pl = self.longitudes[i]
                pl2 = self.latitudes[i]
               
                print('[',pl,',',pl2,']',',')
                i += 1

                if i == 15:
                    break
            else:
                pl = self.longitudes[i]
                pl2 = self.latitudes[i]
                print('L.latLng(',pl,',',pl2,')',',')
               
                i += 1

                if i == 15:
                    break

           


lg= input('enter longitude: ')
l = input('enter latitude: ')
lg2 = input ('enter final longitude: ')
l2 = input('enter final latitude ')
sf = stepfinder(lg,l,lg2,l2)

sf.stepcalc()

