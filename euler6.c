#include<stdio.h>
#include<math.h>

int main()
{
  int square_sum = 0;
  int sum_square = 0;
  int sum = 0;
  int total = 0;
  for(int x = 1 ; x < 101 ; x++)
  {
    total = total + x;
  }
  square_sum = pow(total,2);
  for(int y = 1 ; y < 101 ; y++)
  {
    int a = pow(y,2);	  
    sum_square = sum_square + a;
  }
  sum = square_sum - sum_square;
  printf("The difference is %i\n",sum);
}
