# arduino.py

# Listens on COM3 for data to arrive, then triggers Events to SimConnect based on a Dictionary which maps the data received with the Event Name

from SimConnect import *  #Requires SimConnect from https://pypi.org/project/SimConnect/ (pip install SimConnect)
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
"B": "PITOT_HEAT_TOGGLE"
}

def decodeCommand(command):
    command = command.decode('utf-8') #Cleans what was received in the serial port to what is wanted
    simCommand = commandDict.get(command)
    print (str(simCommand) + " received")
    return simCommand

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
