
// single_button.ino

//set button and led pins
const int ledPin = 5;
const int buttonPin = 9;

//define variables
int ledState = HIGH;         // the current state of the output pin
int buttonState;             // the current reading from the input pin
int lastButtonState = HIGH;   // the previous reading from the input pin
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers

void setup() 
{
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);  
 
   // set initial LED state
  digitalWrite(ledPin, ledState);
  Serial.begin(9600);  
}

void loop() 
{
  //Check the status of the button and store in a variable
  int currentButtonState = digitalRead(buttonPin);

  // If the switch changed, due to noise or pressing:
  if (currentButtonState != lastButtonState) {
    // reset the debouncing timer
    lastDebounceTime = millis();
  }
  
  if ((millis() - lastDebounceTime) > debounceDelay) {
    // whatever the reading is at, it's been there for longer than the debounce
    // delay, so take it as the actual current state:

    // if the button state has changed:
    if (currentButtonState != buttonState) {
      buttonState = currentButtonState;

      // only toggle the LED if the new button state is HIGH
      if (buttonState == HIGH) {
        ledState = !ledState;
        Serial.write('B');
      }
    }
  }
  
  // set the LED:
  digitalWrite(ledPin, ledState);
 

  // Next time through the loop, it'll be the lastButtonState:
  lastButtonState = currentButtonState;
  }
