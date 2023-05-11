#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * check_cycle - checks if linked list is looped
 * @list: start position of linked list
 *
 * Return: 1 (list is looped), otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *temp2 = list;

	if (!list || (list->next == NULL))
		return (0);

	while (temp2 != NULL && temp2->next != NULL && temp != NULL)
	{
		temp = temp->next;
		temp2 = temp2->next->next;

		if (temp == temp2)
			return (1);
	}

	return (0);
}
