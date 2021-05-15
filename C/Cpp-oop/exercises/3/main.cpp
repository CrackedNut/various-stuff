#include <iostream>

using namespace std;

class Animal
{
protected:
  string name;
  int age;
public:
  Animal(string n, int a){
    name = n;
    age = a;
  }
  void set_name(string n) {
    name = n;
  }
  void speak() {
    cout << "I'm an animal called " << name << " of age " << age << endl;
  }
};

class Zebra: public Animal
{
public:
  Zebra(string n, int a):Animal(n,a){};

  void speak() {
    cout << "I am a Zebra named " << name << " of age " << age << endl;
  }
};

class Penguin: public Animal
{
public:
  Penguin(string n, int a):Animal(n,a){};

  void speak() {
    cout << "I am a Penguin named " << name << " of age " << age << endl;
  }
};

int main(int argc, char const *argv[]) {

  Animal a("Marco", 69);
  a.speak();
  Zebra z("DioZebra", 420);
  z.speak();
  Penguin p("DioPinguino", 1337);
  p.speak();
  p.set_name("Pingu");
  p.speak();

  return 0;
}
