#include<stdio.h>
int main()
{
  int first = 0, sum = 0, total = 0;
  int last = 1;
  while (total < 4000000) 
  {
    sum = first + last;
    if(sum % 2 == 0)
    {
      total = total + sum;
    }
    first = last;
    last = sum;
    sum = 0;
  }
  printf("The sum is %i\n",total);
  return 0;
}
