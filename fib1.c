// done using recursion
#include<stdio.h>
int fib(int n) {
    if(n==0)
        return 0;
    else if(n==1)
        return 1;
    else
        return fib(n-1) + fib(n-2);
}
int main() 
{
    int num;
    printf("Enter the number: ");
    scanf("%d", &num);
    int f = fib(num);
    printf("The corresponding number in fibonacci is: %d\n", f);
}