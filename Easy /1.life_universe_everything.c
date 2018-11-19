#include<stdio.h>

int main()
{
	int x,j,c=0,i=0,a[100];
	while(c!=42)
	{
		scanf("%d",&x);
		c=x;
		a[i]=x;
		i++;
	}
	for(j=0;j<i-1;j++)
		printf("\n%d",a[j]);
	return(0);
}
