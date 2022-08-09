#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a number into a sorted list
 * @head: p-t-p to a linkedlist
 * @number: number to be inserted
 * Return: address of the new node, NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nuevo = NULL, *prev = NULL, *siguiente = NULL;


	if (!head)
		return (NULL);
	nuevo = malloc(sizeof(listint_t));
	if (!nuevo)
		return (NULL);
	nuevo->n = number;
	if (!*head)
		return (*head = nuevo);
	if (number <= (*head)->n)
	{
		nuevo->next = *head;
		return (*head = nuevo);
	}
	prev = *head;
	siguiente = prev->next;
	while (siguiente)
	{
		if (siguiente->n >= number)
			break;
		prev = siguiente;
		siguiente = siguiente->next;
	}
	prev->next = nuevo;
	nuevo->next = siguiente;
	return (nuevo);
}
