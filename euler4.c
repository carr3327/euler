#include<stdio.h>

int is_pal(int n);

int main()
{
	int sum;
	int total = 0;
	for(int x = 999; x > 500; x--)
	{
		for(int y = 999; y > 500; y--)
		{
			sum = x * y;
			if ( is_pal(sum) != 0 )
			{
				if ( sum > total)
				{
					total = sum;
				}
				break;
			}
		}
	}
	printf("%d\n",total);
}

int is_pal(int n)
{
	int t, r =0;
	t = n;
	while (t != 0)
	{
		r = r * 10;
		r = r + t%10;
		t = t/10;
		if (n == r)
		{
			return  n;
		}
	}
	return 0;
}
