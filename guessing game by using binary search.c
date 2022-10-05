#include<stdio.h>
int main()
{
	int arr[1000],low=0,high=1000,mid,ans,count=0,i;
	while(low<=high)
	{
		mid=(low+high)/2;
		printf("is your number is %d\n press 1. correct\n press 2. no,it is less than %d\n press 3.no,it is greater than %d\n",mid,mid,mid);
		scanf("%d",&ans);
		count++;
		if(ans==1)
		{
			printf("\n");
			printf("the number is %d\n",mid);
			printf("the number of questio0ns asked was %d\n",count);
			i++;
			break;
		}
		else if(ans==2)
		{
			high=mid+1;
		}
		else
		{
			low = mid-1;
		}
		printf("\n");
	}
}
