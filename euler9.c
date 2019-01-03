#include<stdio.h>
#include<math.h>

int main()
{
	//Using Dickson's methon for generating Pythagorean triples
	//x = r + s
	//y = r + t
	//z = r + s + t 
	//r2 = (r**2)/2
	size_t s,r,t,r2,x,y,z;
	for( r = 2; r < 1000; r+=2)
	{
		r2 = (pow(r,2))/2; 
		for ( s = 1; s <sqrt(r2); s++)
		{
			if ( r2 % s == 0)
			{
				t = r2 / s;
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
