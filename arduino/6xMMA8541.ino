#include "Wire.h"
extern "C" { 
#include "utility/twi.h"  // from Wire library, so we can do bus scanning
}

#include <Adafruit_Sensor.h>
#include <Adafruit_MMA8451.h> 

Adafruit_MMA8451 pos1  = Adafruit_MMA8451();
Adafruit_MMA8451 pos2  = Adafruit_MMA8451();
Adafruit_MMA8451 pos3  = Adafruit_MMA8451();
Adafruit_MMA8451 pos4  = Adafruit_MMA8451();

Adafruit_MMA8451 pos5  = Adafruit_MMA8451();
Adafruit_MMA8451 pos6  = Adafruit_MMA8451();
 
 
#define TCAADDR 0x70
 
void tcaselect(uint8_t i) {
  if (i > 7) return;
 
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}

 boolean running = true;
 
// standard Arduino setup()
void setup()
{
    while (!Serial);
    delay(1000);
 
    Wire.begin();
    
    Serial.begin(115200);
    Serial.println("\nTCAScanner ready!");
    
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

    tcaselect(0);
      if(! pos1.begin(0x1D))
      {
        /* There was a problem detecting the HMC5883 ... check your connections */
        Serial.println("No MMA8451 detected in position 1!");
        running = false;
        while(1);
      } else {
        Serial.println("Position 1 ready to go!");
      }

      tcaselect(1);
      if(! pos2.begin(0x1D))
      {
        /* There was a problem detecting the HMC5883 ... check your connections */
        Serial.println("No MMA8451 detected in position 2!");
        running = false;
        while(1);
      } else {
        Serial.println("Position 2 ready to go!");
      }
            tcaselect(2);
      if(! pos3.begin(0x1D))
      {
        /* There was a problem detecting the HMC5883 ... check your connections */
        Serial.println("No MMA8451 detected in position 3!");
        running = false;
        while(1);
      } else {
        Serial.println("Position 3 ready to go!");
      }

            tcaselect(3);
      if(! pos4.begin(0x1D))
      {
        /* There was a problem detecting the HMC5883 ... check your connections */
        Serial.println("No MMA8451 detected in position 4!");
        running = false;
        while(1);
      } else {
        Serial.println("Position 4 ready to go!");
      }

      tcaselect(4);

            if(! pos5.begin(0x1D))
      {
        /* There was a problem detecting the HMC5883 ... check your connections */
        Serial.println("No MMA8451 detected in position 5!");
        running = false;
        while(1);
      } else {
        Serial.println("Position 5 ready to go!");
      }


tcaselect(5);
            if(! pos6.begin(0x1D))
      {
        /* There was a problem detecting the HMC5883 ... check your connections */
        Serial.println("No MMA8451 detected in position 6!");
        running = false;
        while(1);
      } else {
        Serial.println("Position 6 ready to go!");
      }

      pinMode(11, OUTPUT);

}
 
void loop() 
{

  
      if(running) {
        digitalWrite(11, HIGH);
      }
      
  pos1.read();
    tcaselect(0);
    sensors_event_t pos1_event;
    pos1.getEvent(&pos1_event);

    
    tcaselect(1);
    sensors_event_t pos2_event;
    pos2.getEvent(&pos2_event);

        tcaselect(2);
    sensors_event_t pos3_event;
    pos3.getEvent(&pos3_event);

        tcaselect(3);
    sensors_event_t pos4_event;
    pos4.getEvent(&pos4_event);

    
        tcaselect(4);
    sensors_event_t pos5_event;
    pos5.getEvent(&pos5_event);

        tcaselect(5);
    sensors_event_t pos6_event;
    pos6.getEvent(&pos6_event);

    int delayer = millis();

//    if( (delayer % 5) == 0 ) {


    Serial.print("1,"); Serial.print(pos1_event.acceleration.x); 
    Serial.print(","); Serial.print(pos1_event.acceleration.y); 
    Serial.print(","); Serial.print(pos1_event.acceleration.z); 
    Serial.print("\n");
// 
//
//    Serial.print(",2,"); Serial.print(pos2_event.acceleration.x); 
//    Serial.print(","); Serial.print(pos2_event.acceleration.y); 
//    Serial.print(","); Serial.print(pos2_event.acceleration.z); 
//
//        Serial.print("\t\tPos 3 X: "); Serial.print(pos3_event.acceleration.x); 
//    Serial.print("  Y: "); Serial.print(pos3_event.acceleration.y); 
//    Serial.print("  Z: "); Serial.print(pos3_event.acceleration.z);
//
//        Serial.print("\t\tPos 4 X:"); Serial.print(pos4_event.acceleration.x);
//    Serial.print("  Y: "); Serial.print(pos4_event.acceleration.y);
//    Serial.print("  Z: "); Serial.print(pos4_event.acceleration.z);
// 
//            Serial.print("\t\tPos 5 X: "); Serial.print(pos5_event.acceleration.x); 
//    Serial.print("  Y: "); Serial.print(pos5_event.acceleration.y); 
//    Serial.print("  Z: "); Serial.print(pos5_event.acceleration.z);
//
//        Serial.print("\t\tPos 6 X:"); Serial.print(pos6_event.acceleration.x);
//    Serial.print("  Y: "); Serial.print(pos6_event.acceleration.y);
//    Serial.print("  Z: "); Serial.print(pos6_event.acceleration.z);
    
//    Serial.println("     m/s^2 ");
    
//    }

}
