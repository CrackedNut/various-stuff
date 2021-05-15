#include <iostream>
#include <string>
#include <sstream>

using namespace std;

class MyClass
{
  private:
    int myNum;
    string myString;

  public:
    void setNum(int n) {
      myNum = n;
    }
    int getNum(){
      return myNum;
    }
    void setStr(string s) {
      myString = s;
    }
    string getString(){
      return myString;
    }
    MyClass(string s, int n)
    {
      myNum = n;
      myString = s;
    }
};

int main(int argc, char const *argv[]) {
  stringstream str;
  str << argv[2]; int x; str >> x;
  MyClass first("Hello", 1);
  MyClass fromArg(argv[1], x);
  cout << first.getString() << endl;
  cout << first.getNum() << endl;
  cout << fromArg.getString() << endl;
  cout << fromArg.getNum() << endl;
  return 0;
}
