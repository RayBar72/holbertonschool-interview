#include "search.h"

/**
 * linear_skip - function that searches for a value in a sorted skip
 * list of integers.
 * @list: pointer to head of linked list
 * @value: value to be searched
 * Return: a pointer to the searched value or NULL
 */

skiplist_t *linear_skip(skiplist_t *list, int value)
{
	skiplist_t *recorre = list;

	if (!list)
		return (NULL);
	
	while (recorre->express)
	{
		printf("Value checked at index [%lu] = [%d]\n",
			recorre->express->index, recorre->express->n);
		if (recorre->express->n >= value)
		{
			printf("Value found between indexes [%lu] and [%lu]\n",
				recorre->index, recorre->express->index);
			break;
		}
		recorre = recorre->express;
	}
	if (!recorre->express)
	{
		for (list = recorre; list->next; list = list->next)
			;
		printf("Value found between indexes [%lu] and [%lu]\n",
				recorre->index, list->index);
	}
	for (list = recorre; list != recorre->express; list = list->next)
	{
		printf("Value checked at index [%lu] = [%d]\n", list->index, list->n);
		if (value == list->n)
			break;
	}
	if (list == recorre->express)
		return (NULL);
	else
		return (list);
}
