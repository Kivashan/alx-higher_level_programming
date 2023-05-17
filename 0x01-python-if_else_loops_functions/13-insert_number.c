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
	int flag = 0;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!head)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	temp = *head;
	while (temp && (temp->n < number))
	{
		flag = 1;
		if ((temp->next && (temp->next->n > number)) || !temp->next)
			break;
		temp = temp->next;
	}
	if (flag == 1)
	{
		new->next = temp->next;
		temp->next = new;
	}
	else
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	return (new);
}
