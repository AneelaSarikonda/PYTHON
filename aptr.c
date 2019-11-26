#include<stdio.h>
int main() 
{ 
  
    // Pointer to an array of five numbers 
   //int(*a)[5];
int *a;
    //int *a[5]; 
  
    int b[5] = { 1, 2, 3, 4, 5 }; 
     
    int *p1 = (&b+1);
    int *p2 = b+1;
    int i = 0; 
  
    // Points to the whole array b 
 
    printf("%p %p %d\n",b,p2,*p1); 
    a = &b; 
  
    for (i = 0; i < 5; i++)
        printf("%d\t",(*a+i));
//	printf("%d\t",*(a+1));
      // printf("%d\n", *(a + i)); 
  
    return 0; 
} 
