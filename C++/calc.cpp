#include <stdio.h>

using namespace std;

int main()
{
  float fnum, snum, res;
  int cho;

  printf("1. Addizone\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione\n5. Esci\n");

  while(true)
  {
    printf("Scelta: ");
    scanf("%d\n",cho);
    printf("Primo numero: ");
    scanf("%f\n",fnum);
    printf("Secondo numero: ");
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

    printf("Risultato= %.2f", res);

  }
}
