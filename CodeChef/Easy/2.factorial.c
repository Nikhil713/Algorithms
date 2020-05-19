#include<stdio.h>

int main()
{
	int i,no,a,c5;
	scanf("%d",&no);
	int b[no];
	for(i=0;i<no;i++)
	{
		scanf("%d",&a);
		c5=0;
		while(a>=5)
		{
			c5+=a/5;
			a/=5;
		}
		b[i]=c5;
	}
	for(i=0;i<no;i++)
		printf("%d\n",b[i]);
}
