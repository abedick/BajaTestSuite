/*****
* Object: Accelerometer Data Conversion
* Description: Functions that convert data between analogue and digital values.
* For: JMS Baja (jmsbaja.org)
* Author: William Graham
* Modified: April 15, 2017
* License: ???
*****/

#include "Accelerometer_Conversion.h"

//Converts a double to an integer
int Accelerometer_Conversion::doubleToInteger(double d){
  int value = d * 100;

  //when d is negative find the radix complement
  if(value < 0){
    value += 1000;
  }

  return value;
}

//Converts the digital information in an double that is <= 5
double Accelerometer_Conversion::analogueValue(double d1, double d2, double d3){
  int x = 0, y = 0, z = 0;
  int value = 0;

  x = doubleToInteger(d1);
  y = doubleToInteger(d2);
  z = doubleToInteger(d3);

  value = (x * 1000000) + (y * 1000) + (z);

  return (value * 1.0) / 199999999.8;
}
