/* This program is used to find 
the largest prime factor of a number */


#include<stdio.h>
#include<math.h>

int Lprime(int num)
{
int big;
while(num%2==0)
	{big=2;
	num/=2;
	}
for(int i=3;i<=num/2;i+=2)
	{
	while(num%i==0)
		{big=i;
		num/=i;
		}
	}
if(num>2)
	big=num;

return big;
}





void main()
{
int T,N,i,maxprime;
printf("Enter the no of test cases\n");
scanf("%d",&T);
for(i=1;i<=T;i++)
	{printf("\nEnter the number\n");
	scanf("%d",&N);
	maxprime=Lprime(N);
	printf("the largest prime is %d \n",maxprime);
	}


}
	
