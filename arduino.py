# arduino.py

# Listens on COM3 for data to arrive, then triggers Events to Microsoft Flight Simulator S2020 via Python-SimConnect based on a Dictionary which maps the data received with the Event Name
# Works with an Arduino board with two-way switches which are configured to send respective data
# At this stage only the PITOT HEAT switch and FUEL PUMP switch are implemented

from SimConnect import *  #Requires Python-SimConnect from https://pypi.org/project/SimConnect/ (pip install SimConnect)
import serial  #Requires pySerial (pip install pyserial)

# Create connection to Sim
sm = SimConnect()
ae = AircraftEvents(sm)
aq = AircraftRequests(sm, _time=2000)

# Create connection to Arduino
ser = serial.Serial('COM3', 9600)

def trigger_event(event_name, value_to_use = None):
    #This is where the event is triggered to SimConnect
	event_to_trigger = ae.find(event_name)
	if event_to_trigger is not None:
		if value_to_use is None:
			event_to_trigger()
		else:
			event_to_trigger(int(value_to_use))

		status = "success"
	else:
		status = "Error: %s is not an Event" % (event_name)

	return status

#Dictionary to provide SimConnect Events
commandDict = {
"A": "FUEL_PUMP",
"B": "PITOT_HEAT_TOGGLE",
"C": "LANDING_LIGHTS_TOGGLE"
}

def decodeCommand(command):
    command = command.decode('utf-8') #Cleans what was received in the serial port to what is wanted
    simCommand = commandDict.get(command)
    print (str(simCommand) + " received")
    return simCommand

print("Ready...")

while True:
    command = ser.read()
    if command:
        # flush serial for unprocessed data
        ser.flushInput()
        #Decode and trigger command in Sim
        trigger_event(decodeCommand(command))

# Disconnect and exit
sm.exit()
exit()
