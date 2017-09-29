

//
//
//   @file: 
//   @author: Abe Dick
//   @date: 9/21/2017
//   @desc:
//
//



#include <Wire.h>

extern "C" { 
  #include "utility/twi.h"
}

#include <Adafruit_Sensor.h>
#include <Adafruit_MMA8451.h> 

#include <Adafruit_L3GD20_U.h>
#include "SD.h"
#include "RTClib.h"
#include <SD.h>
#include <SPI.h>

#include <LiquidCrystal.h>

// -------------------------------------------------------------------------------------------------------
// -- setup 6 potential accelerometers using an array
// -------------------------------------------------------------------------------------------------------


Adafruit_MMA8451 accel_1 = Adafruit_MMA8451();
Adafruit_MMA8451 accel_2 = Adafruit_MMA8451();
Adafruit_MMA8451 accel_3 = Adafruit_MMA8451();
Adafruit_MMA8451 accel_4 = Adafruit_MMA8451();
Adafruit_MMA8451 accel_5 = Adafruit_MMA8451();
Adafruit_MMA8451 accel_6 = Adafruit_MMA8451();

Adafruit_L3GD20 gyro = Adafruit_L3GD20();

// -------------------------------------------------------------------------------------------------------
// -- setup the multiplexor
// -------------------------------------------------------------------------------------------------------
#define TCAADDR 0x70
 
void tcaselect(uint8_t i) {
  if (i > 7) return;
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}

// -------------------------------------------------------------------------------------------------------
// -- initialize SD card reader
// -------------------------------------------------------------------------------------------------------

// A simple data logger for the Arduino analog pins

// how many milliseconds between grabbing data and logging it. 1000 ms is once a second
#define LOG_INTERVAL  1000 // mills between entries (reduce to take more/faster data)

// how many milliseconds before writing the logged data permanently to disk
// set it to the LOG_INTERVAL to write each time (safest)
// set it to 10*LOG_INTERVAL to write all data every 10 datareads, you could lose up to 
// the last 10 reads if power is lost but it uses less power and is much faster!
#define SYNC_INTERVAL 1000 // mills between calls to flush() - to write data to the card
uint32_t syncTime = 0; // time of last sync()

#define ECHO_TO_SERIAL   1 // echo data to serial port
#define WAIT_TO_START    0 // Wait for serial input in setup()

// the digital pins that connect to the LEDs
#define redLEDpin 2
#define greenLEDpin 3

// The analog pins that connect to the sensors
#define photocellPin 0           // analog 0
#define tempPin 1                // analog 1
#define BANDGAPREF 14            // special indicator that we want to measure the bandgap

#define aref_voltage 3.3         // we tie 3.3V to ARef and measure it with a multimeter!
#define bandgap_voltage 1.1      // this is not super guaranteed but its not -too- off

RTC_DS1307 RTC; // define the Real Time Clock object

// for the data logging shield, we use digital pin 10 for the SD cs line
const int chipSelect = 10;

// the logging file
File logfile;

void error(char *str)
{
  Serial.print("error: ");
  Serial.println(str);
  
  // red LED indicates error
  digitalWrite(redLEDpin, HIGH);

  while(1);
}

// -------------------------------------------------------------------------------------------------------
// -- Initialize variables
// -------------------------------------------------------------------------------------------------------

boolean setup_complete = true;
boolean print_to_serial_monitor = true;
boolean print_to_sd = true;

// LED pins


const int setup_complete_led_pin = 44;
const int readbuttonPin = 48;     
const int readledPin =  46;   

const int idlebuttonPin = 49;     
const int idleledPin =  42; 

int readbuttonState = 0;
int idlebuttonState = 0;

// -------------------------------------------------------------------------------------------------------
// -- Arduino setup()
// -------------------------------------------------------------------------------------------------------

void setup()
{

  // Open the I^2C Bus
  Wire.begin();

  // -------------------------------------------------------------------------------------------------------
  // -- Setup the LCD Display
  // -------------------------------------------------------------------------------------------------------

  Wire.beginTransmission(12); // transmit to device #8
  Wire.write(2);              // sends one byte
  Wire.endTransmission();    // stop transmitting

  // -------------------------------------------------------------------------------------------------------
  // -- Connect to the multiplexor
  // -------------------------------------------------------------------------------------------------------

  // Setup the serial protocal and choose the port to display the serial monitor
  while (!Serial);
  delay(1000);
 
  Serial.begin(9600);

  // Mux scanner
  Serial.println("\nMux ready");

  for (uint8_t t=0; t<8; t++) {
    tcaselect(t);
    Serial.print("TCA Port #"); Serial.println(t);
 
    for (uint8_t addr = 0; addr<=127; addr++) {
    if (addr == TCAADDR) continue;
    uint8_t data;

    if (! twi_writeTo(addr, &data, 0, 1, 1)) {
       Serial.print("Found I2C 0x");  Serial.println(addr,HEX);
    }
    }
  }
  Serial.println("\ndone");

  // -------------------------------------------------------------------------------------------------------
  // -- setup SD card reader
  // -------------------------------------------------------------------------------------------------------

  Serial.print("Initializing SD card.");
  pinMode(10, OUTPUT);

  if (!SD.begin(chipSelect)) {
    error("Card failed, or not present");
  }
  Serial.println("card initialized.");
  
  // create a new file
  char filename[] = "LOGGER00.CSV";
  for (uint8_t i = 0; i < 100; i++) {
    filename[6] = i/10 + '0';
    filename[7] = i%10 + '0';
    if (! SD.exists(filename)) {
      // only open a new file if it doesn't exist
      logfile = SD.open(filename, FILE_WRITE); 
      break;  // leave the loop!
    }
  }

    Serial.println(logfile);
    

    if (! logfile) {
    error("couldnt create file");
    }
  
  Serial.print("Logging to: ");
  Serial.println(filename);

  if (!RTC.begin()) {
    logfile.println("RTC failed");
  #if ECHO_TO_SERIAL
    Serial.println("RTC failed");
  #endif  //ECHO_TO_SERIAL
    }
    
   
  logfile.println("g_x,g_y,g_z,a1_x,a1_y,a1_z,a2_x,a2_y,a2_z,a3_x,a3_y,a3_z,a4_x,a4_y,a4_z,a5_x,a5_y,a5_z,a6_x,a6_y,a5_z");
  Serial.println("g_x,g_y,g_z,a1_x,a1_y,a1_z,a2_x,a2_y,a2_z,a3_x,a3_y,a3_z,a4_x,a4_y,a4_z,a5_x,a5_y,a5_z,a6_x,a6_y,a5_z");

  // -------------------------------------------------------------------------------------------------------
  // -- setup the accelerometors
  // -------------------------------------------------------------------------------------------------------

  tcaselect(0);
  if(! accel_1.begin(0x1D)) { 
    Serial.println("An MMA8451 was not detected in position 1"); 
    setup_complete = false; 
    while(1);
  } else { Serial.println("Ready at position 1");}

  tcaselect(1);
  if(! accel_2.begin(0x1D)){
    Serial.println("An MMA8451 was not detected in position 2");
    setup_complete = false;
    while(1);
  } else { Serial.println("Ready at position 2");}

  tcaselect(2);
  if(! accel_3.begin(0x1D)){
    Serial.println("An MMA8451 was not detected in position 3");
    setup_complete = false;
    while(1);
  } else { Serial.println("Ready at position 3"); }

  tcaselect(3);
  if(! accel_4.begin(0x1D)) {
    Serial.println("An MMA8451 was not detected in position 4");
    setup_complete = false;
    while(1);
  } else { Serial.println("Ready at position 4"); }

  tcaselect(4);
  if(! accel_5.begin(0x1D)) {
    Serial.println("An MMA8451 was not detected in position 5");
    setup_complete = false;
    while(1);
  } else { Serial.println("Ready at position 5"); }

  tcaselect(5);
  if(! accel_6.begin(0x1D)) {
    Serial.println("An MMA8451 was not detected in position 6");
    setup_complete = false;
    while(1);
  } else { Serial.println("Ready at position 6"); }

  if (!gyro.begin()) {
    Serial.println("Gyro not Ready");
    setup_complete = false;
    while (1);
  } else { Serial.println("Gyro Ready"); }

  // -------------------------------------------------------------------------------------------------------
  // -- Complete setup
  // -------------------------------------------------------------------------------------------------------

  pinMode(readledPin, OUTPUT);      
  pinMode(readbuttonPin, INPUT_PULLUP);   

  pinMode(idleledPin, OUTPUT);      
  pinMode(idlebuttonPin, INPUT_PULLUP);   

  digitalWrite(idleledPin, HIGH);  

  if(setup_complete) {
    digitalWrite(setup_complete_led_pin, HIGH);
    Wire.beginTransmission(12); // transmit to device #8
    Wire.write(1);              // sends one byte
    Wire.endTransmission();    // stop transmitting
  } else {
    digitalWrite(setup_complete_led_pin, LOW);
    Wire.beginTransmission(12); // transmit to device #8
    Wire.write(5);              // sends one byte
    Wire.endTransmission();    // stop transmitting
  }


}
 
void loop() 
{
  // -------------------------------------------------------------------------------------------------------
  // -- Grab events from each accelermoter via the mux channel
  // -------------------------------------------------------------------------------------------------------

   gyro.read();
  
   accel_1.read();
   tcaselect(0);
   sensors_event_t accel_1_event;
   accel_1.getEvent(&accel_1_event);

   tcaselect(1);
   sensors_event_t accel_2_event;
   accel_2.getEvent(&accel_2_event);

   tcaselect(2);
   sensors_event_t accel_3_event;
   accel_3.getEvent(&accel_3_event);

   tcaselect(3);
   sensors_event_t accel_4_event;
   accel_4.getEvent(&accel_4_event);

   tcaselect(4);
   sensors_event_t accel_5_event;
   accel_5.getEvent(&accel_5_event);

   tcaselect(5);
   sensors_event_t accel_6_event;
   accel_6.getEvent(&accel_6_event);

  // -------------------------------------------------------------------------------------------------------
  // -- Print events to the serial monitor
  // -------------------------------------------------------------------------------------------------------

  if(print_to_sd){
    logfile.print(gyro.data.x); 
    logfile.print(","); logfile.print(gyro.data.y); 
    logfile.print(","); logfile.print(gyro.data.z); 
      
    logfile.print(","); logfile.print(accel_1_event.acceleration.x); 
    logfile.print(","); logfile.print(accel_1_event.acceleration.y); 
    logfile.print(","); logfile.print(accel_1_event.acceleration.z); 
    
    logfile.print(","); logfile.print(accel_2_event.acceleration.y); 
    logfile.print(","); logfile.print(accel_2_event.acceleration.z); 
    logfile.print(","); logfile.print(accel_2_event.acceleration.x); 
    
    logfile.print(","); logfile.print(accel_3_event.acceleration.x); 
    logfile.print(","); logfile.print(accel_3_event.acceleration.y); 
    logfile.print(","); logfile.print(accel_3_event.acceleration.z);
    
    logfile.print(","); logfile.print(accel_4_event.acceleration.x);
    logfile.print(","); logfile.print(accel_4_event.acceleration.y);
    logfile.print(","); logfile.print(accel_4_event.acceleration.z);
     
    logfile.print(","); logfile.print(accel_5_event.acceleration.x); 
    logfile.print(","); logfile.print(accel_5_event.acceleration.y); 
    logfile.print(","); logfile.print(accel_5_event.acceleration.z);
    
    logfile.print(","); logfile.print(accel_6_event.acceleration.x);
    logfile.print(","); logfile.print(accel_6_event.acceleration.y);
    logfile.print(","); logfile.print(accel_6_event.acceleration.z);
  logfile.print("\n");
}
  if(print_to_serial_monitor){
    Serial.print(gyro.data.x); 
    Serial.print(","); Serial.print(gyro.data.y); 
    Serial.print(","); Serial.print(gyro.data.z); 
    
   Serial.print("0,"); Serial.print(accel_1_event.acceleration.x); 
   Serial.print(","); Serial.print(accel_1_event.acceleration.y); 
   Serial.print(","); Serial.print(accel_1_event.acceleration.z); 
  
   Serial.print(","); Serial.print(accel_2_event.acceleration.x); 
   Serial.print(","); Serial.print(accel_2_event.acceleration.y); 
   Serial.print(","); Serial.print(accel_2_event.acceleration.z); 
  
   Serial.print(","); Serial.print(accel_3_event.acceleration.x); 
   Serial.print(","); Serial.print(accel_3_event.acceleration.y); 
   Serial.print(","); Serial.print(accel_3_event.acceleration.z);
  
   Serial.print(","); Serial.print(accel_4_event.acceleration.x);
   Serial.print(","); Serial.print(accel_4_event.acceleration.y);
   Serial.print(","); Serial.print(accel_4_event.acceleration.z);
   
   Serial.print(","); Serial.print(accel_5_event.acceleration.x); 
   Serial.print(","); Serial.print(accel_5_event.acceleration.y); 
   Serial.print(","); Serial.print(accel_5_event.acceleration.z);
  
   Serial.print(","); Serial.print(accel_6_event.acceleration.x);
   Serial.print(","); Serial.print(accel_6_event.acceleration.y);
   Serial.print(","); Serial.print(accel_6_event.acceleration.z);
   Serial.print("\n");

    print_to_serial_monitor = false;
  }

    if ((millis() - syncTime) < SYNC_INTERVAL) return;
  syncTime = millis();
  logfile.flush();

//  
//  readbuttonState = digitalRead(readbuttonPin);
//  idlebuttonState = digitalRead(idlebuttonPin);
//
//  if( readbuttonState == HIGH) {
//      print_to_serial_monitor = true;
//
//      digitalWrite(readledPin, HIGH);
//      digitalWrite(idleledPin, LOW);
//      Wire.beginTransmission(12);
//      Wire.write(4);
//      Wire.endTransmission();
//    } 
//    
//  if (idlebuttonState == HIGH ) {
//    print_to_serial_monitor = false;
//    
//    digitalWrite(readledPin, LOW);
//    digitalWrite(idleledPin, HIGH);
//    Wire.beginTransmission(12);
//    Wire.write(3);
//    Wire.endTransmission();
//  }



}
