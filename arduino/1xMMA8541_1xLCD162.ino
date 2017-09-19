#include <Wire.h>                                     // I2C Wire Library

// Adafruit Libraries
#include <Adafruit_MMA8451.h>                         // https://github.com/adafruit/Adafruit_MMA8451_Library
#include <Adafruit_Sensor.h>                          // https://github.com/adafruit/Adafruit_Sensor

//Defining the object for each sensor, mma and mma2
Adafruit_MMA8451 mma  = Adafruit_MMA8451();
//Sample using LiquidCrystal library
#include <LiquidCrystal.h>

/*******************************************************

  This program will test the LCD panel and the buttons

********************************************************/

// select the pins used on the LCD panel
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

// define some values used by the panel and buttons
int lcd_key     = 0;
int adc_key_in  = 0;
#define btnRIGHT  0
#define btnUP     1
#define btnDOWN   2
#define btnLEFT   3
#define btnSELECT 4
#define btnNONE   5


boolean writing = false;

int ledPinR = 2; 

// read the buttons
int read_LCD_buttons()
{
  adc_key_in = analogRead(0);      // read the value from the sensor
  // my buttons when read are centered at these valies: 0, 144, 329, 504, 741
  // we add approx 50 to those values and check to see if we are close
  if (adc_key_in > 1000) return btnNONE; // We make this the 1st option for speed reasons since it will be the most likely result
  // For V1.1 us this threshold
  if (adc_key_in < 50)   return btnRIGHT;
  if (adc_key_in < 250)  return btnUP;
  if (adc_key_in < 450)  return btnDOWN;
  if (adc_key_in < 650)  return btnLEFT;
  if (adc_key_in < 850)  return btnSELECT;

  return btnNONE;  // when all others fail, return this...
}

void setup()
{
  lcd.begin(16, 2);                                     // start the library
  lcd.setCursor(0, 0);                                  // print a simple message
  Serial.begin(9600);                                   // Initiate serial communication


  lcd.print("Baja Test Suite");
  delay(2500);
  lcd.setCursor(0, 2);
  lcd.print("(c) 2017 KUBAJA");
  delay(1000);

  Serial.println("Start");
  if (! mma.begin(0x1D)) {                            // First sensor in the address of 0x1C
    Serial.println("Couldnt start first sensor");
    while (1);
  }

  Serial.println("Good");
  mma.setRange(MMA8451_RANGE_4_G);
  
}

void loop()
{
  

  mma.read();                                         // Read data for the first sensor

  int value = millis();

  if ((value % 3) == 0) {
    /* Get a new sensor event */
    sensors_event_t event;
    //  sensors_event_t event2;
    mma.getEvent(&event);
    //  mma2.getEvent(&event2);

    /* Display the results (acceleration is measured in m/s^2) */
    lcd.clear();
    lcd.print("X:"); lcd.print((double)event.acceleration.x,2);

    lcd.setCursor(8, 0);
    lcd.print(" Y:"); lcd.print((double)event.acceleration.y,2);

      lcd.setCursor(0,2);
       lcd.print("z:"); lcd.print(event.acceleration.z,2);

     if(writing == true) { lcd.setCursor(9, 2); lcd.print("**"); }


    Serial.print("X: \t"); Serial.print(event.acceleration.x); Serial.print("\t");
    Serial.print("Y: \t"); Serial.print(event.acceleration.y); Serial.print("\t");
    Serial.print("Z: \t"); Serial.print(event.acceleration.z); Serial.print("\t");
    Serial.println("m/s^2 ");

  }




  lcd.setCursor(0, 1);           // move to the begining of the second line
  lcd_key = read_LCD_buttons();  // read the buttons

  switch (lcd_key)               // depending on which button was pushed, we perform an action
  {
    case btnRIGHT:
      {
        lcd.print("RIGHT ");
        break;
      }
    case btnLEFT:
      {
        lcd.print(adc_key_in);
        lcd.print(" v");
        break;
      }
    case btnUP:
      {
        lcd.print("UP    ");
        break;
      }
    case btnDOWN:
      {   
        if(writing == true) {
           writing = false;
           digitalWrite(ledPinR, LOW);
        } else {
          writing = true;
          digitalWrite(ledPinR, HIGH);
        }

        break;
      }
    case btnSELECT:
      {
        lcd.print("SELECT");

        break;
      }
    case btnNONE:
      {
        break;
      }
  }

}