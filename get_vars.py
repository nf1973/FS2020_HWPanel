# get_vars.py

# Gets and display Simulation variables from Microsoft Flight Simulator S2020 via Python-SimConnect

from SimConnect import *  #Requires Python-SimConnect from https://pypi.org/project/SimConnect/ (pip install SimConnect)

def getSimVarDict():
    varDict = {}
    varDict["LATITUDE"] = aq.get("PLANE_LATITUDE")
    varDict["LONGITUDE"] = aq.get("PLANE_LONGITUDE")
    varDict["MAGNETIC_COMPASS"] = round(aq.get("MAGNETIC_COMPASS"))
    varDict["VERTICAL_SPEED"] = round(aq.get("VERTICAL_SPEED"))
    varDict["PITOT_HEAT"] = aq.get("PITOT_HEAT")
    varDict["LIGHT_LANDING_ON"] = aq.get("LIGHT_LANDING_ON")

    return varDict

# Create connection to Sim
sm = SimConnect()
ae = AircraftEvents(sm)
aq = AircraftRequests(sm, _time=2000)

#Load the variables from the Sim
simVariables = getSimVarDict()

#Print all variables and values to the Console
for key, value in simVariables.items():
   print (key + ":", value)

# Disconnect and exit
sm.exit()
exit()
