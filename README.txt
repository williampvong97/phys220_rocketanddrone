LAST UPDATED: May 04 2018 - 07:19 PM - PST

delaystuff/

This is the folder that contains the files from our testing of the arduino code's delay lines. We believe that in the RisingData.ino file, at lines 87 and 89, 

  digitalWrite(LedPin, HIGH);
  delay(50);
  digitalWrite(LedPin, LOW);
  delay(50);

that the argument must be added to find the true delay between data line prints in the Arduino payload. This means for the code above, after one line of data is written to the SD card, the next line of data is written 100ms afterward. We have tested this for different combinations, like

  digitalWrite(LedPin, HIGH);
  delay(1000);
  digitalWrite(LedPin, LOW);
  delay(0);
  
or 
  
  digitalWrite(LedPin, HIGH);
  delay(900);
  digitalWrite(LedPin, LOW);
  delay(100);
  
and we still obtain the same length of time of data-write-timestep, which we'll call dt. The folder called run1/ is our first trial where we tested the data collection lasting 60s and folder run2/ is a trial for 120s. 
