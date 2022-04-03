#include<stdio.h>
void main()
{
    int n;
    printf("enter the total no of elements :");
    scanf("%d",&n);
    int a[n],i,j,k=0;
    for(i=0;i<n;i++)
    {
        printf("enter the number %d:",i+1);
        scanf("%d",&a[i]);
        k=k+a[i];
    }
    j=k/n;
    printf("avrage of the array is%d:",j);

}