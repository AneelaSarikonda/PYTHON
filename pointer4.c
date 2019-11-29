#include<stdio.h>
void mystery(int *ptra, int *ptrb) 
{
   int *temp;
   temp = ptrb;
   ptrb = ptra;
   ptra = temp;
printf("fun==%d\t %d\t",*ptra,*ptrb);
}
int main() 
{
    int a=2016, b=0, c=4, d=42;
    mystery(&a, &b);
printf("a,b values are:%d\t %d\n",a,b);
/*    if (a < c)
       mystery(&c, &a);
printf("a,c values are:%d\t %d\n",a,c);
    mystery(&a, &d);
printf("a and d values are:%d\t%d\n",a,d);
    printf("%d\n", a);*/
}
