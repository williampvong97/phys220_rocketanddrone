#include <SPI.h>
#include <SD.h>
#include <Wire.h>
#include <SparkFunLSM9DS1.h>

const int LedPin = 3;
const int chipSelect = 10;
LSM9DS1 NineDoF;
#define MAG_ADDRESS  0x1E 
#define AG_ADDRESS  0x6B  

void setup() {
  Serial.begin(115200);
  init_SD();
  init_9DoF();
  write_header();
  Serial.println("Starting Data Aquisition...");
  pinMode(LedPin, OUTPUT); 
}

void init_SD(){
  Serial.println("Initializing SD card..."); 
  if (!SD.begin(chipSelect)) {
    Serial.println("Initialization Failed"); 
    while (1);
  }
  Serial.println("Initialization Succeeded");
}

void init_9DoF(){
  Serial.println("Initializing 9DoF..."); 
  NineDoF.settings.device.commInterface = IMU_MODE_I2C;
  NineDoF.settings.device.mAddress = MAG_ADDRESS;
  NineDoF.settings.device.agAddress = AG_ADDRESS;
  if (!NineDoF.begin())
  {
    Serial.println("Initialization Failed"); 
    while (1);
  }
  NineDoF.setAccelScale(16);
  File dataFile = SD.open("datalog.csv", FILE_WRITE);
  if (dataFile) {
    dataFile.println();
  }
  else
  {
    Serial.println("Initialization Failed"); 
    while (1);
  }
  Serial.println("Initialization Succeeded");
  
}

void write_header(){
  Write("Ax");  
  Write("Ay");
  Write("Az");
  Write("Gx");  
  Write("Gy");
  Write("Gz");
  Write("Mx");  
  Write("My");
  Write("Mz");
  WriteEnd("T");
}

void loop() {
  
  NineDoF.readAccel();
  Write(NineDoF.calcAccel(NineDoF.ax));  
  Write(NineDoF.calcAccel(NineDoF.ay));
  Write(NineDoF.calcAccel(NineDoF.az));
  
  NineDoF.readGyro();
  Write(NineDoF.calcGyro(NineDoF.gx));  
  Write(NineDoF.calcGyro(NineDoF.gy));
  Write(NineDoF.calcGyro(NineDoF.gz));
  
  NineDoF.readMag();
  Write(NineDoF.calcMag(NineDoF.mx));  
  Write(NineDoF.calcMag(NineDoF.my));
  Write(NineDoF.calcMag(NineDoF.mz));

  WriteEnd(calibrateSensor(readTempSensor()));

  digitalWrite(LedPin, HIGH);
  delay(50); // 50 ms
  digitalWrite(LedPin, LOW);
  delay(50); // 50 ms
}
int readTempSensor(){
  int sensorValue = analogRead(A3);
  return sensorValue;
}

float calibrateSensor(int raw){
  float y1 = 13; //cold deg C
  float y2 = 55; //hot deg C
  float x1 = 211; //cold adu
  float x2 = 372; //hot adu
  
  float m = (y2-y1)/(x2-x1);
  float b = y1 - m* x1;
  return raw*m+b;
}


void Write(const char* value){
  Serial.print(value); 
  Serial.print(",");
  File dataFile = SD.open("datalog.csv", FILE_WRITE);
  if (dataFile) {
    dataFile.print(value);
    dataFile.print(",");
    dataFile.close();   
  }
}

void Write(float value){
  Serial.print(value); 
  Serial.print(",");
  File dataFile = SD.open("datalog.csv", FILE_WRITE);
  if (dataFile) {
    dataFile.print(value);
    dataFile.print(",");
    dataFile.close();   
  }
}
void WriteEnd(const char* value){
  Serial.print(value);  
  Serial.print("\n"); 
  File dataFile = SD.open("datalog.csv", FILE_WRITE);
  if (dataFile) {
    dataFile.print(value);
    dataFile.println();
    dataFile.close();   
  }
}
void WriteEnd(float value){
  Serial.print(value);  
  Serial.print("\n"); 
  File dataFile = SD.open("datalog.csv", FILE_WRITE);
  if (dataFile) {
    dataFile.print(value);
    dataFile.println();
    dataFile.close();   
  }
}

