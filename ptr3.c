#include<stdio.h>
void fun(int arr[],int n)
{
  int i;
//printf("%d \t%d",sizeof(arr),sizeof(arr[0]));
 // int arr_size = sizeof(arr)/sizeof(arr[0]);
 // printf("%d",arr_size);  
for (i = 0; i < n; i++)
      printf("%d ", arr[i]);
}
 
int main()
{
  int i,n;
  int arr[4] = {10, 20 ,30, 40};
 n = sizeof(arr)/sizeof(arr[0]);
  fun(arr,n);
  return 0;
} 
