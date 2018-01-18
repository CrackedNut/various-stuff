#define RED 6
#define GREEN 5
#define BLUE 4

void red()
{
  digitalWrite(RED, HIGH);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);
}

void green()
{
  digitalWrite(RED, LOW);
  digitalWrite(GREEN, HIGH);
  digitalWrite(BLUE, LOW);
}

void blue()
{
  digitalWrite(RED, LOW);

void setup()
{
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
}

void loop(){
  red();
  delay(500);
  green();
  delay(500);
  blue();
  delay(500);
  }
