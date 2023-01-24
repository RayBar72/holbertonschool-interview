#include "lists.h"

/**
 * find_listint_loop - function that detects loop in linked list
 * @head: pointer to the list
 * Return: pointer to the first node in the loop
*/

listint_t *find_listint_loop(listint_t *head)
{
	listint_t *par = head, *non =head;

	if (!head)
		return (NULL);

	while (par && par->next)
	{
		non = non->next;
		par = par->next->next;
		if (non == par)
		{
			non = head;
			while (non != par)
			{
				non = non->next;
				par = par->next;
			}
			return (non);
		}
	}
	return (NULL);
}
