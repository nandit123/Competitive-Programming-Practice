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
        int jump = 2;
        while(jump < arr_count)
        {
            int maxInstant = arr[i];
            for(j=i+jump;j<arr_count;j+=jump)
            {
                if(arr[j] + maxInstant > maxInstant)
                    maxInstant = arr[j] + maxInstant;
                // maxInstant = max(maxInstant, arr[j-2]+arr[j]);
            }
            maxSum = max(maxSum, maxInstant);
            jump++;
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