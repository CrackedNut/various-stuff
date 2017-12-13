#include "SR04.h"

#define TRIG_PIN 12
#define ECHO_PIN 11
#define R 1
#define Y 2
#define G 3
#define BPIN 5

char stato;
long a;

SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);

void rosso() {
  digitalWrite(R, HIGH);
  digitalWrite(Y, LOW);
  digitalWrite(G, LOW);
  delay(8000);
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
  pinMode(R, OUTPUT);
  pinMode(Y, OUTPUT);
  pinMode(G, OUTPUT);
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  a=sr04.Distance();
  Serial.print(a);
    Serial.println("cm");
  rosso();
  while(a>sr04.Distance()){
    tone(BPIN, 587, 250);
    delay(250);
    tone(BPIN, 440, 250);
    delay(250);
  }

  giallo();
  verde();
}


