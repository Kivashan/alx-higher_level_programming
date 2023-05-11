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
	listint_t *temp;

	if (!list || (list->next != NULL))
		return (0);

	temp = list->next;

	while (temp->next != NULL)
	{
		if (temp == list)
			return (1);

		temp = temp->next;
	}

	return (0);
}
