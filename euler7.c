#include<stdio.h>
#include<math.h>

int is_prime(int n);


int main()
{
  int count = 1;
  for(int x = 2 ; x < 1000000; x++)
  {
	if ( count == 10001)
	{
		printf("The 10,001st prime is %d\n",x);
		break;
	}
	if ( is_prime(x) == x)
	{
		count+=1;
	}
  }
}

int is_prime(int n)
{
	int a = sqrt(n);
	for(int x = 2; x <= a; x++)
	{
		if ( n % x == 0)
		{
			return 0;
		}
	}
	return n;
}
