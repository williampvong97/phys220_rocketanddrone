This file was LAST UPDATED: May 04 2018 - 08:11 PM - PST

!HOW TO DOWNLOAD FILES! ################################################################################################################

If you're interested in downloading any files in this repository but don't know how to, here are some instructions to do so:
1) Go to file that you wish to download
2) Find and click "Raw". It should be next to the buttons "Blame" and "History".
3) You'll be sent to another page and that's fine. Right-click on any part of the page and click "Save as..."

Note that some file extension types are not supported (like .ino), so you may have to end up copy-pasting the file, but you can do that 
as well.

delaystuff/ folder info: ###############################################################################################################

This is the folder that contains the files from our testing of the arduino code's delay lines. We believe that in the RisingData.ino 
file, at lines 87 and 89, 

  digitalWrite(LedPin, HIGH);
  delay(50);
  digitalWrite(LedPin, LOW);
  delay(50);

that the argument must be added to find the true delay between data line prints in the Arduino payload. This means for the code above,
after one line of data is written to the SD card, the next line of data is written 100ms afterward. We have tested this for different 
combinations, like

  digitalWrite(LedPin, HIGH);
  delay(1000);
  digitalWrite(LedPin, LOW);
  delay(0);
  
or 
  
  digitalWrite(LedPin, HIGH);
  delay(900);
  digitalWrite(LedPin, LOW);
  delay(100);
  
and we still obtain the same length of time of data-write-timestep, which we'll call dt. The folder called run1/ is our first trial 
where we tested the data collection lasting 60s and folder run2/ is a trial for 120s. 

In the file handcalculations.jpg, we define a scaling factor k and we get the same value of 2.5 for k for both trials. We may test 
longer trials like a 30min trial (we won't, but it's still something to think about) to see if k = 2.5 still holds for longer periods of 
time. 

What this k-value tells us, is that using dt from the Arduino code isn't enough. For our payload case, if you only use dt = 100ms (the 
default), then you will see that the total time interval of your data collection is only 40% of what you expect it to be, based off our 
k-value from our two trials. This is very important because this means that whatever total time interval you think your data collection 
ranges from, you need to multiply it, at least in our specific payload, by the factor of k = 2.5. Note that this k-value may not be 
universal, so it may be best if you try running some trials to see if you can get a proportional scaling constant for your time 
measurements, like we include in folders run1/ and run2/.

rocketstuff/ folder info: ##############################################################################################################

e20wmotorcurve_CONTROL.jpg is a picture of company-provided information of the motor we used for our rocket. 

We highlight specifically the graph of the motor's thrust force vs. time to compare with our file e20wmotorcomparison.svg. Our rocket 
data, including the adjustments made to our time scale using k = 2.5, horrifically models the thrust-time curve very closely in both 
magnitude and time scale. This allows us to comfortably stick with our k-value adjustment for our calculations.
