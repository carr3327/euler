#include<stdio.h>
#include<math.h>

int main()
{
	size_t s,r,t,tt,x,y,z;
	for( r = 2; r < 1000; r+=2)
	{
		tt = (pow(r,2))/2; 
		for ( s = 1; s <sqrt(tt); s++)
		{
			if ( tt % s == 0)
			{
				t = tt / s;
				x = r + s;
				y = r + t;
				z = r + s + t;
				if ( x + y + z == 1000)
				{
					int sum = 1;
					sum = x * y * z;
					printf("x: %zu, y: %zu, z: %zu sum: %i\n",x,y,z,sum);
				}
			}
		}
	}	
}
