#include<stdio.h>
int main() 
{ 
    // Pointer to an integer 
    int *p; 
    // Pointer to an array of 5 integers 
    int (*ptr)[5];  
    //int *p1[5];
    int arr1[5];  
    // Points to 0th element of the arr. 
    p = &arr1;                             
    // Points to the whole array arr. 
    ptr = &arr1;        
  //  p1=&arr1;
    printf("p = %p, ptr = %p, ", p, ptr);       
    p++;  
    ptr++; 
//    p1++;
    printf("p = %p, ptr = %p, ", p, ptr); 
   
    return 0; 
} 
