#include<stdio.h>
int main()
{
unsigned int a[4][3]={{1,2,3},{4,5,6},{7,8,9},{10,11,12}};


printf("%u\n %d\n %d\n",a+3,*(a+3),*(a+2)+3);



}
