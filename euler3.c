#include<stdio.h>
#include<math.h>

int is_prime(int n);
int lpf(long long n); //Largest prime factor

int main (){
  int result = 0;
  long long pos_prime = 600851475143;
  result = lpf(pos_prime);
  printf("Largest Prime Factor: %d\n", result); 
  return 0;
}

int is_prime(int n){
  int x = 2;
  while ( x <= sqrt(n) )
    if ( n % x == 0)
      return 0;
    else
      x++;
  return n;
}

int lpf(long long n){
  int x = 2;
  int largest = 0;
  while ( x < sqrt(n) ){ 
    if ( ( is_prime(x) == x ) && ( n % x == 0 ) && ( x > largest ) ){
        largest = x;
    }
    else{
      x++;
    }
  }
  return largest;
}
