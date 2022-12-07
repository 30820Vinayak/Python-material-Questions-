#include<stdio.h>
int main()
{
	int i,n,target,f=1;
	printf("enter no of elements");
	scanf("%d",&n);
	printf("enter the digits");
	int arr[n];
	for (i=0;i<n;i++)
	{
	   scanf("%d",arr[n]);
    }
    for (i=0;i<n;i++)
	{
		if (arr[i]==target)
		{
			printf("%d fount at location %d",target,i);
			f=0;
		}
		
	}
	if(f==1)
		{
			printf("Element not found");
		}
		return 0;
}
