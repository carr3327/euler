#include<stdio.h>
#include<math.h>

//The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//Find the sum of all the primes below two million.

int is_prime(long n);

int main (){
        long long sum = 0;
        for( long i= 2; i < 2000000; i++){
                if ( is_prime(i) == i ) {
                        sum += i;
                }
        }
        printf("%lli is the sum of all the primes below two million.\n", sum);
}

int is_prime(long n){
        short int x = 2;
        while ( x <= sqrt(n) ) {
                if ( n % x == 0 ) {
                        return 0;
                }
                else{
                        x++;
                }
        }
        return n;
}
