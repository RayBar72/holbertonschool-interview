#include "sort.h"

/**
 * radix_sort - sorts an array of integers in ascending order using the Radix
 * sort algorithm
 * @array: array to be sorted
 * @size: size of the array
 */
void radix_sort(int *array, size_t size)
{
	int *tmp, max = 0, exp = 1, i;

	if (!array || size < 2)
		return;
	tmp = malloc(sizeof(int) * size);
	if (!tmp)
		return;
	for (i = 0; i < (int)size; i++)
	{
		if (array[i] > max)
			max = array[i];
	}
	while (max / exp > 0)
	{
		int bucket[10] = {0};

		for (i = 0; i < (int)size; i++)
			bucket[array[i] / exp % 10]++;
		for (i = 1; i < 10; i++)
			bucket[i] += bucket[i - 1];
		for (i = (int)size - 1; i >= 0; i--)
			tmp[--bucket[array[i] / exp % 10]] = array[i];
		for (i = 0; i < (int)size; i++)
			array[i] = tmp[i];
		print_array(array, size);
		exp *= 10;
	}
	free(tmp);
}
