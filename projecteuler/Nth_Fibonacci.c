/* This program is used to find the 
      first N digit  Fibonacci Number  */


#include<stdio.h>

int digits(int num)
{
int digit=0;
while(num!=0)
	{digit+=1;
	num/=10;
	}
return digit;

} 


int main()
{
int X0,Y1,count,T,N,i;
printf("enter the test cases\n");
scanf("%d", &T);
for(i=1;i<=T;i++)
	{printf("\nEnter the Number\n");
	scanf("%d", &N);
	X0=1;
	Y1=1;
	count=2;
	while(N!=1)
		{if(count%2==0)
			{X0=X0+Y1;
			if(digits(X0)==N)
				{printf("The first fibonaci with %d digit is %d \n",N,X0);
				break;}			
			}

		else
			{Y1=X0+Y1;
			if(digits(Y1)==N)
				{printf("The first fibonaci with %d digit is %d \n",N,Y1);
				break;}			
			}

		count+=1;


		}
	if(N==1)
				
		printf("The first fibonacci with %d digit is 1\n",N);

	}



}

