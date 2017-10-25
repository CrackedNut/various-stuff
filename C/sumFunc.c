#include <stdio.h>
 //Compiler version gcc 6.3.0


int sum(int num1, int num2)
{
	int summ = num1 + num2;
	return summ;
}

int main(void)
{
	int a, b, res;
	printf("A: ");
	scanf("%d",a);
	
	printf("B: ");
	scanf("%d", b);
	
	res = sum(a, b);
	
	printf("%d",res);
}