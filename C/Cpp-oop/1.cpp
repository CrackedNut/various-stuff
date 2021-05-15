#include <iostream>

using namespace std;


int main() {

  int* b = new int[5];

  for(int i= 0; i < 5; i++)
    b[i] = i + 1;

  cout << b << endl;
  cout << &b << endl;

  for(int i = 0; i < 5; i++)
    cout << b[i] << endl;

  for(int i = 0; i < 5; i++)
    cout << &b[i] << endl;
  delete [] b;


  return 0;
}
