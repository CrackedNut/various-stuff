#include "SR04.h"

#define R 2
#define Y 3
#define G 4
#define BPIN 7
#define TRIG_PIN 12
#define ECHO_PIN 11
int del = 0;

SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);

void rosso() {
  digitalWrite(R, HIGH);
  digitalWrite(Y, LOW);
  digitalWrite(G, LOW);
}

void giallo() {
  digitalWrite(R, LOW);
  digitalWrite(Y, HIGH);
  digitalWrite(G, LOW);
  delay(3000);
}

void verde() {
  digitalWrite(R, LOW);
  digitalWrite(Y, LOW);
  digitalWrite(G, HIGH);
  delay(5000);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(R, OUTPUT);
  pinMode(Y, OUTPUT);
  pinMode(G, OUTPUT);
  Serial.begin(9600);
  delay(500);
  tone(BPIN, 440, 50);
}

void loop() {
  // put your main code here, to run repeatedly:
  do {
    rosso();
    while(sr04.Distance()<20) {
      tone(BPIN, 587, 100);
      delay(100);
      tone(BPIN, 440, 100);
      delay(100);
    }
    delay(250);
    del++;
  } while(del<32);
  del = 0;
  giallo();
  verde();
}











