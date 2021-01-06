from tkinter import *
from SimConnect import *  #Requires SimConnect from https://pypi.org/project/SimConnect/ (pip install SimConnect)

# Create connection to Sim
sm = SimConnect()
ae = AircraftEvents(sm)
aq = AircraftRequests(sm, _time=2000)

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


#Trigger the event
#trigger_event("PITOT_HEAT_TOGGLE")

#Set up the window
gui = Tk()
gui.title("FS2020-HWPanel - UI Test")
gui.geometry("500x200")


#Add buttons
Button(gui, text="PITOT HEAT", width = 10, command=lambda: trigger_event("PITOT_HEAT_TOGGLE")) .grid(row=0, column=0, sticky=W)
Button(gui, text="FUEL_PUMP", width = 10, command=lambda: trigger_event("FUEL_PUMP")) .grid(row=0, column=1, sticky=W)


#loop
gui.mainloop()

# Disconnect and exit
sm.exit()
exit()
