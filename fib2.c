// done using dynamic programming
#include<stdio.h>
int fib(int n) {
    int f[n+2];
    f[0] = 0;
    f[1]=1;

    for(int i=2; i<=n;i++)
    {
        f[i]=f[i-1]+f[i-2];
    }    
    return f[n];
}
int main() 
{
    int num;
    printf("Enter the number: ");
    scanf("%d", &num);
    int f = fib(num);
    printf("The corresponding number in fibonacci is: %d\n", f);
}