#include<stdio.h>
#include<limits.h>
int max(int a, int b)
{
    return (a>b)?a:b;
}
int dp[100005]; // it is dynamic programming array, which contains solution (maxArraySum) till the current index
int maxSubsetSum(int arr_count, int *arr)
{
    dp[0] = max(0, arr[0]);
    if(arr_count==1)
        return dp[0];
    for(int i=0;i<arr_count;i++)
    {
        dp[i] = max(dp[i-2], max(dp[i-1], dp[i-2]+arr[i]));
        printf("dp[%d] is: %d \n", i, dp[i]);
    }
    return max(dp[arr_count-1], dp[arr_count-2]);
}
int main()
{
    int arr[] = {3,7,4,6,5};
    int arr_count = 5;
    int max = maxSubsetSum(arr_count, arr);
    printf("maximum sum is %d. \n", max);
}