#include <stdio.h>

using namespace std;

int main()
{
  int num, fa;
  scanf("Factorial of: %.i\n",num);
  fa = num;
  for(int a = num-1, a>0, a--)
  {
    num = num * a;
  }

  printf("%i!= %i", fa, num)
  return 0;
}
