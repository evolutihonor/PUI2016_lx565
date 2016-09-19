import json
import urllib as ulr
from pprint import pprint
import sys

firstarg = sys.argv[1]
secondarg = sys.argv[2]
def businfo(firstarg,secondarg):
        myapikey="664103a6-4090-4861-a8fc-0305205d43af"

        url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+firstarg+"&VehicleMonitoringDetailLevel=calls&LineRef="+secondarg
        response = ulr.urlopen(url)
        data = response.read().decode("utf-8")
        data = json.loads(data)


        MonitoredVehicleJourney = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']
        busline = MonitoredVehicleJourney['LineRef']
        VehicleActivity = (data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

        n =len(VehicleActivity)
        listofLA=[]
        listofLO=[]
        for i in range(n):
                listofLA.append(VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
                listofLO.append(VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
        print ("Bus Line: %s" %((busline)[-3:]))
        print ("Number of Active Buses : %d"% (n)) 
        for i in range(n):
            print ("Bus %d is at latitude %f and longitude %f" %(i, listofLA[i], listofLO[i]))
      
                                
businfo(firstarg,secondarg)
