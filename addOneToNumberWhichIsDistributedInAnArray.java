public class Solution {
    public int[] plusOne(int[] A) {
        int i,j;
        int len = A.length;
        int flag = 0;
        if(A[len-1]!=9)
        {
            A[len-1]++;
        }
        else
        {
            i=len-1;
            while(A[i]==9 && i!=0)
            {
                A[i] = 0;
                i--;
            }
            if(A[i]!=9) // this checks for index 0 and as well as other indexes
            {
                A[i]++;
            }
            else // this checks for index 0
            {
                A[i] = 0;
                int[] B = new int[len+1];
                B[0] = 1;
                for(j=0;j<len;j++)
                {
                    B[1+j]=A[j];
                }
                flag=1;
                if(B[0]!=0)
                    return B;
                    
                    
                int v=0;
                int lenB=len+1;
                for(i=0;i<lenB;i++)
                {
                    if(B[i]==0)
                        v++;
                    else
                        break;
                }
                int len2 = lenB-v;
                int[] C = new int[len2];
                for(i=0;i<len2;i++)
                {
                    C[i]=B[i+v];
                }
                return C;
            }
        }
        if(A[0]!=0)
            return A;
        int v=0;
        for(i=0;i<len;i++)
        {
            if(A[i]==0)
                v++;
            else
                break;
        }
        int len2 = len-v;
        int[] C = new int[len2];
        for(i=0;i<len2;i++)
        {
            C[i]=A[i+v];
        }
        return C;
    }
}

