#include <iostream>

using namespace std;

class Vehicle
{
protected:
  string brand;

public:

  Vehicle(string b)
  {
    brand = b;
  }

  void honk() {
    cout << "Beep beep mothafucka, I'm a fucking " << brand << " \n";
  }
};

class Car: public Vehicle
{
private:
  string model;
public:
  Car(string b, string m) : Vehicle(b)
  {
    model = m;
  }

  void honk() {
    cout << "I'm a " << brand << " " << model << " now, bitch\n";
  }
};

int main(int argc, char const *argv[]) {
  Vehicle minivan("Ford");
  Car cobra("Shelby", "Cobra");
  minivan.honk();
  cobra.honk();
  return 0;
}
