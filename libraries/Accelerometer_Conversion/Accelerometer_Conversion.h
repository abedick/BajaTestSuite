/*****
* Object: Accelerometer Data Conversion
* Description: Functions that convert data between analogue and digital values.
* For: JMS Baja (jmsbaja.org)
* Author: William Graham
* Modified: April 15, 2017
* License: ???
*****/

/*****
* The functions below are intended to be used to convert digital data
* retrieved from an three axis accelerometer into a single integer.
* They are then supposed to convert back to the three values. To make this
* work I am using an integer as described below.
*
* First off x, y, and z (three values) fall in this order:
*   First is the x value
*   Second is the y value
*   Third is the z value
*
* For each x, y, and z there are three digits:
*   The first two digits represent the whole part of the number.
*   The final is the first decimal of the force of acceleration.
*   The number is in radix complement form.
*
* The final integer should look something like this:
*   143068054 (xxxyyyzzz)
*
* This standard is used for all the calculations to store and retrieve the x, y, and z
*
* The analogue value should be five or less
*****/

#ifndef ACCELEROMETER_CONVERSION
#define ACCELEROMETER_CONVERSION

class Accelerometer_Conversion{
  public:
    static int doubleToInteger(double d);
    static double analogueValue(double d1, double d2, double d3);
};

#endif
