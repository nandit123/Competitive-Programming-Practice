// done using dynamic programming
#include<stdio.h>
int fib(int n) {
    int a=0, b=1, c, i;
    if(n==0)
        return 0;
    for(i=2;i<=n;i++)
    {
        c=a+b;
        a=b;
        b=c;
    }    
    return b;
}
int main() 
{
    int num;
    printf("Enter the number: ");
    scanf("%d", &num);
    int f = fib(num);
    printf("The corresponding number in fibonacci is: %d\n", f);
}