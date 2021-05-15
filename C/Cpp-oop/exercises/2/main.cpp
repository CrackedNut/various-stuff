#include <iostream>

using namespace std;

class Mother
{
public:
  void display()
  {
    cout << "Mother\n";
  }
};

class Daughter: public Mother
{
public:
  void display(){
    cout << "Daughter!\n";
  }
};

int main(int argc, char const *argv[]) {

  Daughter d;

  d.display();

  return 0;
}
