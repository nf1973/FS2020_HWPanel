
// single_button.ino

//set button and led pins
const int switchAPin = 7;   
const int switchBPin = 8; 
const int switchCPin = 9; 


int currentSwitchAState;
int lastSwitchAState;

int currentSwitchBState;
int lastSwitchBState;

int currentSwitchCState;
int lastSwitchCState;

//Send the serial output only if the switch state has changed
int triggerEventIfStateChanged (int lastState, int currentState, String command)
{
    if (lastState!=currentState) {
      Serial.print(command);
      return 1;
    }
    return 0;
}
  
void setup() 
{
  pinMode(switchAPin, INPUT_PULLUP);  
  pinMode(switchBPin, INPUT_PULLUP);  
  pinMode(switchCPin, INPUT_PULLUP);
   
  Serial.begin(9600);

  //Initially set the "last" states to the current state to try and avoid a change being detected the first time the loop runs.
  lastSwitchAState = digitalRead(switchAPin);
  lastSwitchBState = digitalRead(switchBPin);
  lastSwitchCState = digitalRead(switchCPin);
}

void loop() 
{

  delay(50); // slow the loop down to avoid needing to debounce the switches

  //Get Current State of Switches
  currentSwitchAState = digitalRead(switchAPin);
  currentSwitchBState = digitalRead(switchBPin);
  currentSwitchCState = digitalRead(switchCPin);

  //
  triggerEventIfStateChanged(currentSwitchAState, lastSwitchAState, "A");
  triggerEventIfStateChanged(currentSwitchBState, lastSwitchBState, "B");
  triggerEventIfStateChanged(currentSwitchCState, lastSwitchCState, "C");
 
  //Update variables holding last states
  lastSwitchAState = currentSwitchAState;
  lastSwitchBState = currentSwitchBState;
  lastSwitchCState = currentSwitchCState;
  
}
  
