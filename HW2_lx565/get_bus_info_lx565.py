import pylab as pl
import json
import urllib as ulr
import pandas as pd
import sys

listofstop = []
listofstatus = []
stop = []
status = []
myapikey = sys.argv[1]
busline = sys.argv[2]
mycsv = sys.argv[3]
def bus_info(myapikey,busline,mycsv):


        url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+myapikey+"&VehicleMonitoringDetailLevel=calls&LineRef="+busline 
        response = ulr.urlopen(url)

        data = response.read().decode("utf-8")
        data = json.loads(data)

        if not len(sys.argv) == 4:
            print("Invalid number of arguments. Run as: python aPythonScriptThatWritesToCSV.py mycvs.csv")
            sys.exit()

        fout = open(mycsv, "w")
        fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

        VehicleActivity = (data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
        n =len(VehicleActivity)
        listofLA=[]
        listofLO=[]
        #print (VehicleActivity)
        for i in range(n):
                listofLA.append(VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
                listofLO.append(VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
                if (VehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls'] == ''):
                        stop.append('N/A')
                        status.append('N/A')
                else:
                        stop.append(VehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
                        status.append(VehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
            
                fout.write ("%f, %f, %s, %s\n " %(listofLA[i], listofLO[i], stop[i], status[i]))
            
        fout.close()

bus_info(myapikey,busline,mycsv)


