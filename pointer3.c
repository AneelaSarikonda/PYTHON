int main() 
{ 
    int arr[] = {1,2,3,4,5}; 
//    int *p = arr; 
int i,j;
    int (*ptr)[5] = arr; 
/*    printf("p = %p, ptr = %p\n", p, ptr); 
    printf("*p = %d, *ptr = %p\n,ptr[0]=%d\n", *p, *ptr,*ptr[0]); 
    printf("sizeof(p) = %lu, sizeof(*p) = %lu\n",sizeof(p), sizeof(*p)); 
    printf("sizeof(ptr) = %lu, sizeof(*ptr) = %lu\n",sizeof(ptr), sizeof(*ptr)); 
    return 0; */
printf("%p\n",ptr);
ptr++;

printf("%p\n",ptr);

/*
for(i=0;i<5;i++)
{

//printf("%d  %d\n",p[i],*(p+i));

printf("%p  %d\n",ptr[i],ptr[0][i]);
} */
}
