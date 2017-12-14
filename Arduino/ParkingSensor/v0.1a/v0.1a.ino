#include "SR04.h"
#include <math.h> 

#define BPIN 7
#define TRIG_PIN 12
#define ECHO_PIN 11

SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);

long dist;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(1) {
    dist = sr04.Distance();
    Serial.println(dist);
    tone(BPIN,440,50);
    delay(100);
  }
}




