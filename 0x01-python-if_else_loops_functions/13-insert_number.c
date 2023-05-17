#include "lists.h"

/**
 * insert_node - add a node at a specific point in list
 * @head: first node in list
 * @number: integer value, will be used to determine position of new node
 *
 * Return: address of new node on success, Null otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	temp = *head;
	new->n = number;

	while (temp && (temp->n < number))
	{
		if (temp->next && (temp->next->n > number))
			break;
		temp = temp->next;
	}

	new->next = temp->next;
	temp->next = new;

	return (new);
}
