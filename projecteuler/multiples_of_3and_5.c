//Project Euler Problem :1


#include<stdio.h>

///sum of multiples of 3 and 5 

void main()
{
int n,Sum=0;
printf("enter the number\n");
scanf("%d",&n);
for(int i=1;i<n;i++)
{if(i%3==0 || i%5==0)
	{Sum+=i;
	}
}
printf("the sum of multiples : %d",Sum);


}


