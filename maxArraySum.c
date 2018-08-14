#include<stdio.h>
#include<limits.h>
int max(int a, int b)
{
    return (a>b)?a:b;
}
int maxSubsetSum(int arr_count, int *arr)
{
    int maxSum = INT_MIN;
    int i, j;
    for(i=0;i<arr_count-2;i++)
    {
        for(j=i+2;j<arr_count;j++)
        {
            maxSum = max(maxSum, arr[i]+arr[j]);
        }
    }
    return maxSum;
}
int main()
{
    int arr[] = {3,7,4,6,5};
    int arr_count = 5;
    int max = maxSubsetSum(arr_count, arr);
    printf("maximum sum is %d. \n", max);
}