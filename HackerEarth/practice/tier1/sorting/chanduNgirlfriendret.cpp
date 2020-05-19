#include<bits/stdc++.h>

using namespace std;

int main()
{
    int tcase,i,j;
    scanf("%d",&tcase);
    for(i=0;i<tcase;i++)
    {
        int size1,size2;
        scanf("%d %d ",&size1,&size2);

        int array1[size1],array2[size2];
        for(j=0;j<size1;j++)
            scanf("%d",&array1[j]);
        for(j=0;j<size2;j++)
            scanf("%d",&array2[j]);
        
        int size3=size1+size2;
        int array3[size3];   
        
        for(j=0;j<size1;j++)
            array3[j]=array1[j];
        for(j=size1;j<size3;j++)
            array3[j]=array2[j-size1];
        
        sort(array3, array3+size3, greater<int>());         
        
        for(j=0;j<size3;j++)
            printf("%d ",array3[j]);
        printf("\n");    
    }

    return 0;
}