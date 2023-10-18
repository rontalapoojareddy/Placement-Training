/*main()
{

int a=12;
if(a&1)
{
	printf("odd");
}
else
{
	printf("even");//even
}
}*/
/*main()
{
	int a=15,count=0;
	while(a)
	{
		count++;
		a=a&(a-1);
	}
	printf("count=%d",count);//4
}*/
/*smallest no greater than n with exactly 1 bit diff in binary form
main()
{
	int a=14;
	printf("%d",a|a+1);
}*/
/*main()
{
	int a=15,i=4;
	if(a&(1<<(i-1)))
	{
		printf("yes");//yes
	}
	else
	{
		printf("no");
	}
}*/
//determine a number is power of 2 or not 
/*#include <stdio.h>

int isPowerOfTwo(int num) {
    if (num <= 0) {
        return 0; 
    }
    return (num & (num - 1)) == 0;
}

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (isPowerOfTwo(num)) {
        printf("%d is a power of 2.\n", num);
    } else {
        printf("%d is not a power of 2.\n", num);
    }

    return 0;
}*/
//determine a number is power of 4 or not 
/*#include <stdio.h>
#include <math.h>

int isPowerOfFour(int num) {
    if (num <= 0) {
        return 0; 
    }

    double logValue = log(num) / log(4);
    return (logValue - (int)logValue) == 0;
}

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (isPowerOfFour(num)) {
        printf("%d is a power of 4.\n", num);
    } else {
        printf("%d is not a power of 4.\n", num);
    }

    return 0;
}*/
// power of 2
/*main()
{

int count=0,n=256;
while(n)
{
	count++;
	n=n&(n-1);
}
if(count==1)
printf("true");//true
else
printf("false");
}*/
// power of 4
/*main()
{

int count=0,n=256;
while(n)
{
	count++;
	n=n&(n-3);
}
if(count==1)
printf("true");//true
else
printf("false");
}*/
/*main()
{
if(printf("%d",1))
printf("test");//1test
else
printf("no");
}*/
// 
// missing no
/*main()
{
int a[]={1,2,3,4,5,6,7,9};
int x=0,i=0;
for(i=0;i<=8;i++)
x=x^i;
for(i=0;i<8-1;i++)
x=x^a[i];
printf("%d",x);//8
}*/
/*main()
{
int a[5]={10,20,30,20,10};
int res=0,i=0;
for(i=0;i<5;i++)
{
	res=res^a[i];
}
printf("%d",res);//30
}*/
/*main()
{
int a[]={10,20,30,20,10,35,10};
int res=0,i=0;
for(i=0;i<=6;i++)
{
	res=res^a[i];
//30
}
printf("%d",res);
}*/
// write a factorial no using recursion
/*#include<stdio.h>
int main()
{
	long long int n,i,fact=1;
	scanf("%lld",&n);
	for(i=1;i<=n;i++)
	{
		fact=fact*i;
	}
	printf("%lld",fact);
}
*/
/*#include<stdio.h>
long long int fib(long long int n)
{
	if(n==0||n==1)
	return n;
	else
	return fib(n-1)+fib(n-2);
}
int main() 
{
	long long int n,i;
	scanf("%lld",&n);
	for(i=0;i<n;i++)
	printf("%lld\n",fib(i));
}*/
main()
{
	int n,i;
	
}