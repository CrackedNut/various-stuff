#include <iostream>

using namespace std;

class Shape
{
protected:
  float width;
  float height;
public:
  Shape(float w, float h){
    width = w;
    height = h;
  }
  float area();
};

class Rectangle: public Shape
{
public:
  Rectangle(float w, float h):Shape(w, h){};
  void area(){
    cout << "Area = " << width*height << endl;
  }
};

class Triangle: public Shape
{
public:
  Triangle(float w, float h):Shape(w, h){};
  void area(){
    cout << "Area = " << width*height/2 << endl;
  }
};

int main(int argc, char const *argv[]) {

  Rectangle r(5, 3);
  Triangle t(2, 4);
  r.area();
  t.area();

  return 0;
}
