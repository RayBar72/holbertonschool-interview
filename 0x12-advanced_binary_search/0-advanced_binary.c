#include "search_algos.h"

/**
 * rec_advanced - return the index of the first value in the array
 * @inicial: pointer to the array
 * @recorre: pointer to search in the array
 * @size: size of array
 * @value: value to find
 * Return: index of value or -1
 */
int rec_advanced(int *inicial, int *recorre, size_t size, int value)
{
	size_t mid = (size - 1) / 2, i = 0;

	if (size < 1)
		return (-1);
	printf("Searching in array: ");
	for (i = 0; i < size; i++)
		printf("%d%s", recorre[i], i < size - 1 ? ", " : "\n");

	if (!mid && *recorre >= value)
		return (*recorre == value ? recorre - inicial : -1);
	else if (recorre[mid] >= value)
		return (rec_advanced(inicial, recorre, mid + 1, value));
	return (rec_advanced(inicial, recorre + mid + 1, size - mid - 1, value));
}


/**
 * advanced_binary - return the index of the first value in the array
 * @array: pointer to array to search
 * @size: size of array
 * @value: value to be searched
 * Return: index or -1
 */
int advanced_binary(int *array, size_t size, int value)
{
	return (rec_advanced(array, array, size, value));
}
