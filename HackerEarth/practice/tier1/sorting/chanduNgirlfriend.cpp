#include<iostream>
#include<bits/stdc++.h>
// #include<string>

using namespace std;

int main()
{
    int tcase,i;
    int j,array_size;
    scanf("%d",&tcase);
    
    for(i=0;i<tcase;i++)
    {

        scanf("%d",&array_size);
        int array[array_size];
        for(j=0;j<array_size;j++)
        {
            scanf("%d",&array[j]);
        }

        sort(array, array+array_size, greater<int>());
        for(j=0;j<array_size;j++)
        {
            printf("%d ",array[j]);
        }
        printf("\n" );
    }
    return 0;
}