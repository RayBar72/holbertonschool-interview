#include "sort.h"

/**
 * merge - Function thaat merges two arrays into original
 * @array: Pointer to priamary array
 * @izq: pointer to left array
 * @der: pointer to right array
 * @size: size of the priamary array
*/
void merge(int *array, int *izq, int *der, size_t size)
{
	int s_i, s_d;
	int i = 0, j = 0, k = 0;

	s_i = size / 2;
	s_d = size - s_i;
	printf("Merging...\n");
	printf("[left]: ");
	print_array(izq, s_i);
	printf("[right]: ");
	print_array(der, s_d);

	while (i < s_i && j < s_d)
	{
		if (izq[i] < der[j])
			array[k++] = izq[i++];
		else
			array[k++] = der[j++];
	}

	while (i < s_i)
		array[k++] = izq[i++];

	while (j < s_d)
		array[k++] = der[j++];
	printf("[Done]: ");
	print_array(array, size);
}

/**
 * merge_sort - Function that sort an array in ascending order
 * with merge sort algorithm
 * @array: pointer to array
 * @size: size of the array
*/
void merge_sort(int *array, size_t size)
{
	int der[512];
	int izq[512];
	size_t med = 0, i = 0;

	if (!array)
		return;

	if (size < 2)
		return;

	med = size / 2;

	for (i = 0; i < med; i++)
		izq[i] = array[i];
	for (i = med; i < size; i++)
	{
		der[i - med] = array[i];
	}
	merge_sort(izq, med);
	merge_sort(der, size - med);
	merge(array, izq, der, size);
}
