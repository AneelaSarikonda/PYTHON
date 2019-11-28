#include<stdio.h>
int main()
{
int *a[]={10,20};
char *ptr1[]={"Hii","aaaaaaa"};
char *ptr2="Hello";
printf("%d\t%d\n",a[0],a[1]);
printf("%c\n",*ptr2);
printf("%c\t%c\n",*ptr1[0],*ptr1[1]);
return 0;
}
