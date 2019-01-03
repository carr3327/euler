#include<stdio.h>

int main()
{
  long long number = 2500;
  for (number; number < 240000000; number+= 20)
  { 
    int div = 20;
    while ( div > 0 )
    {
      if (number % div == 0)
      {
        div--;
      }
      else
      {
        break;
      }
     }
  if ( div == 0)
  {
    printf("The answer is %lli\n",number);
    break;
  }
  }
}

