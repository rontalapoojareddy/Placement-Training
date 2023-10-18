/*#include<stdio.h>
#include<stdlib.h>
struct ss
{
	int a;
	float b;
}s1,s2,s3;
main()
{
	printf("sizeof apple=%d",sizeof(s1));//8
}*/
/*#include<stdio.h>
#include<stdlib.h>
struct ss
{
	int a;
	float b;
	char c;
}s1,s2,s3;
main()
{
	printf("sizeof apple=%d",sizeof(s1));//12
}*/
/*#include<stdio.h>
#include<stdlib.h>
struct ss
{
	int a;
	double b;
	char c;
}s1,s2,s3;
main()
{
	printf("sizeof apple=%d",sizeof(s1));//24
}*/
/*#include<stdio.h>
#include<stdlib.h>
struct ss
{
	int a;
	float b;
	char c[100];
}s1,s2,s3;
main()
{
	printf("sizeof apple=%d",sizeof(s1));//108
}*/
/*#include<stdio.h>
#include<stdlib.h>
struct ss
{
	int a;
	double b;
	char c[777];
}s1,s2,s3;
main()
{
	printf("sizeof apple=%d",sizeof(s1));//800
}*/
/*#include<stdio.h>
#include<stdlib.h>
struct ss
{
	int a;
	double b;
	char c[1999];
}s1,s2,s3;
main()
{
	printf("sizeof apple=%d",sizeof(s1));//2016
}*/
/*#include<stdio.h>
#include<stdlib.h>
struct ss
{
	int a[100];
	double b;
	char c[1999];
}s1,s2,s3;
main()
{
	printf("sizeof apple=%d",sizeof(s1));//2408
}*/
/*#include<stdio.h>
#include<stdlib.h>
struct ss
{
	int a[103];
	double b;
	char c[1999];
}s1,s2,s3;
main()
{
	printf("sizeof apple=%d",sizeof(s1));//2424
}*/
/*#include<stdio.h>
#include<stdlib.h>
struct ss
{
	int a[103];
	double b[3000];
	char c[1999];
}s1,s2,s3;
main()
{
	printf("sizeof apple=%d",sizeof(s1));//26416
}*/