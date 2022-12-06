#include "sort.h"

void swap(int *a, int *b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}


void heapify(int *arr, int n, int i, size_t total_size)
{
	int largest = i;
	int left = 2 * i + 1;
	int right = 2 * i + 2;

	if (left < n && arr[left] > arr[largest])
		largest = left;

	if (right < n && arr[right] > arr[largest])
		largest = right;

	if (largest != i)
	{
		swap(&arr[i], &arr[largest]);
		print_array(arr, total_size);
		heapify(arr, n, largest, total_size);
	}
}

void heap_sort(int *array, size_t size)
{
	size_t i;

	if (array)
	{
		for (i = size / 2 - 1; (int)i >= 0; i--)
			heapify(array, size, i, size);

	for (int i = size - 1; (int)i > 0; i--)
	{
			swap(&array[0], &array[i]);
			print_array(array, size);
			heapify(array, i, 0, size);
	}
	}
}
