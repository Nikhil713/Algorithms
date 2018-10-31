#include<stdio.h>

int partition (long int arr[],long int low,long int high)
{
    int temp,temp1;
    int pivot = arr[high];    // pivot
    int i = (low - 1);  // Index of smaller element
    for (int j = low; j <= high- 1; j++)
    {
        // If current element is smaller than or
        // equal to pivot
        if (arr[j] <= pivot)
        {
            i++;    // increment index of smaller element
	    temp=arr[i];
            arr[i]=arr[j];
	    arr[j]=temp;
        }
    }
    temp1=arr[i+1];
    arr[i+1]=arr[high];
    arr[high]=temp1;
    return (i + 1);
}
/* The main function that implements QuickSort
 arr[] --> Array to be sorted,
  low  --> Starting index,
  high  --> Ending index */
void quickSort(long int arr[],long int low,long int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        int pi = partition(arr, low, high);

        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
int main()
{
	int tcase,num,i,j;
	scanf("%d",&tcase);
	scanf("%d",&num);
	long int horse[num];
	for(i=0;i<tcase;i++)
	{
		for(j=0;j<num;j++)
		{
			scanf("%ld",&horse[num]);
		}
	quickSort(horse,horse[0],horse[num]);
	}
	return(0);
}
