/**
* Program: Digital to Analogue converter
* Description: A program that collects data from MMA 8451 accelerometers from Adafruit and sends the x, y, and z values as a analog signal to another system.
* For: JMS Baja (jmsbaja.org)
* Author: William Graham
* Modified: March 21, 2017
* License: ???
**/

#include <Wire.h>
#include <Adafruit_MMA8451.h>
#include <Adafruit_Sensor.h>
#include <Accelerometer_Conversion.h>

/*Setup Each Accelerometer*/
Adafruit_MMA8451 accel2 = Adafruit_MMA8451(0x1C);
Adafruit_MMA8451 accel1 = Adafruit_MMA8451(0x1D);

int numAccels = 0;

void setup(void) {
  Serial.begin(9600);

  //Start working with each accelerometer. If not require a system restart.
  if(!accel1.begin()){
    Serial.println("Accelerometer 1 not found.");
    numAccels += 1;
  }
  
  if(!accel1.begin()){
    Serial.println("Accelerometer 1 not found.");
    numAccels += 1;
  }

  //Do nothing if an accelerometer is not found
  if(numAccels == 0){
    while(true){
      Serial.println("No accelerometers found!");
    }
  }

  //Set the force range (2, 4, or 8)
  accel1.setRange(MMA8451_RANGE_4_G);
}

//Runs while on after setup has finished.
void loop() {
  switch(numAccels){
    case 2:
      readCurrentAcceleration(accel1, 10);
    case 1:
      readCurrentAcceleration(accel1, 9);
      break;
    default:
      Serial.println("No accelerometers!! To far into program.");
  }
}

//Gets the acceleration of the accelerometer
void readCurrentAcceleration(Adafruit_MMA8451 accel, int outPort){
  sensors_event_t event;
  double values[3];

  accel.getEvent(&event);

  values[0] = event.acceleration.x;
  values[1] = event.acceleration.y;
  values[2] = event.acceleration.z;

  writeCurrentAcceleration(outPort, Accelerometer_Conversion::analogueValue(values[0], values[1], values[2]));
}

void writeCurrentAcceleration(int port, double acceleration){
  analogWrite(port, acceleration * 51.0);
}
