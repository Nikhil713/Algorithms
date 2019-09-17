#include<bits/stdc++.h>

using namespace std;

int main()
{
    int tcase;
    int i,j,k;
    int nooffrnds;
    scanf("%d",&tcase);
    for(i=0;i<tcase;i++)
    {
        scanf("%d",&nooffrnds);
        int weights[nooffrnds];
        for(j=0;j<nooffrnds;j++)
        {
            scanf("%d",&weights[j]);            
        }
        for(j=0;j<nooffrnds;j++)
        {
            int count = 0;
            for(k=j+1;k<nooffrnds;k++)
            {
                if(weights[j]>weights[k])
                {
                    count++;
                }
            }
            printf("%d ",count); 
        }
        printf("\n");    
    }
    return 0;
}