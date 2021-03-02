#include <stdio.h>

long long solution(int a, int b)
{   
    long long sum=0;
    int A = a<b?a:b;
    int B = a<b?b:a;
    
    for(int i=A; i<=B; i++)
        sum += i;
    
    return sum;
}
