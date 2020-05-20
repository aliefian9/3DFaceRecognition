#include <Servo.h>

char serialData;
Servo servo;

void setup() {
  servo.attach(9);
  servo.write(0);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() > 0)
    serialData = Serial.read();
    Serial.print(serialData);

    if(serialData == '1'){
      servo.write(90);  
    }
    else if(serialData == '0'){
      servo.write(0);  
    }

}
