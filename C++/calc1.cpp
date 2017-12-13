#include <stdio.h>

using namespace std;

int main()
{
  float fnum, snum, res;
  int cho;

  printf("1. Sum\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n");

  while(true)
  {
    printf("Choice: ");
    scanf("%d\n",cho);
    printf("First number: ");
    scanf("%f\n",fnum);
    printf("Second number: ");
    scanf("%f\n",snum);
    switch (cho)
     {
      case 1:
        res = fnum + snum;
      case 2:
        res = fnum - snum;
      case 3:
        res = fnum * snum;
      case 4:
        res = fnum / snum;
      case 5:
        break;
      default:
        continue;
    }

    printf("Result= %.2f", res);

  }
  return res;
}

