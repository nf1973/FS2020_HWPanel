# FS2020-HWPanel

FS2020-HWPanel leverages [Python-SimConnect](https://github.com/odwdinc/Python-SimConnect) and [pySerial] (https://github.com/pyserial/pyserial) to allow two-way switches connected to an Arduino board to control switches in Microsoft Flight Simulator 2020 (MSFS2020).

This project is in the very initial and early stages of development but is in a working state (at least with the Cessna 172).

## arduino.py

Listens on COM3 for data to arrive, then triggers Events to Microsoft Flight Simulator S2020 via Python-SimConnect based on a Dictionary which maps the data received with the Event Name.
I currently have it working with some simple two-way switches connected to the Arduino.
The code running on the Arduino can be found in 'single_switch.ino'

## gui.py

So that testing could be done without the need for Arduino board this uses a [tkinter] (https://github.com/python/cpython/tree/master/Lib/tkinter/) GUI with buttons to trigger Events to Microsoft Flight Simulator S2020 via Python-SimConnect.

## get_vars.py

Reads Simulator variables out of MSFS2020 (also using Python-SimConnect) and discplays on console.

## Notes

For Python-SimConnect, Python 64-bit is needed.

## Microsoft SimConnect Documentation

Below are links to the Microsoft documentation for SimConnect

[Function](https://docs.microsoft.com/en-us/previous-versions/microsoft-esp/cc526983(v=msdn.10))

[Event IDs](https://docs.microsoft.com/en-us/previous-versions/microsoft-esp/cc526980(v=msdn.10))

[Simulation Variables](https://docs.microsoft.com/en-us/previous-versions/microsoft-esp/cc526981(v=msdn.10))
