# HP3245a_Calibration
Using a Python script to calibrate and adjust an HP3245 precision source with an HP3458a 8.5 digit multimeter.

# The Manual Adjustment:
All but one of the HP3245a adjustments require that you read a series of voltage and current outputs from the instrument and enter the values back into the HP3245a. There are two adjustment options: a full adjustment which consists of 71 readings; 47 of which are voltage, and 24 of which are current. The second option is a voltage adjustment only. Here, only the 47 voltage readings are entered back into the HP3245a. in addition the 10X high voltage output requires the manual adjustment of its offset.

# Modern Times:
Not only is this a pain, it is fraught with error. Fortunately, back in the day, there was a better way involving an HP 9000/300 computer and floppy disks. Now there is once again, a better way: a Python script with PyVISA to control the HP3245a and the HP3458a. Oh, and an operator.

The HP3245a and HP3458a will be connected in two ways: first with a GPIB cable on a network controlled by a computer; second, with a cable from the BNC output of the HP3245a to the input (either fron or back) of the HP3458a. If calibration and adjustment of the current is desired, the operator will be promped to switch the connection on the HP3458a when needed.
