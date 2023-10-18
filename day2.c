/*#include<stdio.h>
int main()
{
	int lemon;
	printf("lemon no");
	scanf("%d",&lemon);
//	(lemon==21)?printf(" the lemons r according to required"):printf("not ");
	(lemon>21)? printf("%d excess lemons",lemon-21):printf(" need %d more lemons",21-lemon);
	//(lemon> 21)? printf("%d excess lemons",lemon-21):printf(" the lemons r nt as required",21-lemon);
	//printf("lemon %d",lemon);
}*/
/*#include<stdio.h>
int main()
{
	int a[10][10],i,n,j,count=0;
	printf(" the value of matrix size");
	scanf("%d",&n);
	printf(" enter the matrix elements");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[i][j]);
		}
		//printf("\n");
	}
	printf(" the matrix is \n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d ",a[i][j]);
		}
		printf("\n");
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(a[i]==a[j])
			{
				count=count+1;		
			}
		//	if(a[i]<a[j])
		}
			
	}
		printf("the 1's left diagonal is %d\n",count);
			printf("the 1's horizontal count\n");
			printf("the 1's vertical count\n");
			printf("the 1's right diagonal count\n");
			printf("the 0's left diagonal is %d\n",count);
			printf("the 0's horizontal count\n");
			printf("the 0's vertical count\n");
			printf("the 0's right diagonal count\n");
			peerfect square root numbers between 40 to 100 write a c program in c
	}*/
#include <stdio.h>
#include <math.h>
int main() 
{
    for (int num = 40; num <= 100; num++) 
	{
        double sn = pow(num,0.5);
        int ins = (int)sn;
        if (ins* ins == num) 
		{
            printf("%d\n", num);
        }
    }
}
