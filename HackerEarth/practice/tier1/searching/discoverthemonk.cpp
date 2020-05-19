#include<bits/stdc++.h>

using namespace std;

int main()
{
    int query,i,j,querysize,arraysize,flag=0;
    scanf("%d %d",&arraysize,&querysize);
    int array[arraysize];
    for(i=0;i<arraysize;i++)
    {
        scanf("%d",&array[i]);
    }
    for(i=0;i<querysize;i++)
    {
        flag=0;
        scanf("%d",&query);
        for(j=0;j<arraysize;j++)
        {
            
            if(query==array[j])
            {
                printf("YES\n");
                flag=1;
                break;
            }
        }
        if(flag==0)
        {
            printf("NO\n");
        }
    }
    return 0;
}