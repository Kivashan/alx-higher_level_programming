#include "lists.h"

int length(listint_t **head);

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: start position of linked list
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int i = 0, sum = 0, len;
	listint_t *temp;

	if (!head)
		return (1);

	temp = *head;
	len = length(head);

	while (i < (len / 2))
	{
		sum += temp->n;
		i++;
	}

	if (len % 2 == 1)
		i++;

	while (i < len)
	{
		sum -= temp->n;
		i++;
	}

	return ((sum == 0) ? 1 : 0);
}

/**
 * length - returns length of linked list
 * @head: the starting position of linked list
 *
 * Return: returns the no of elements in linked list
 */
int length(listint_t **head)
{
	int len = 0;
	listint_t *temp = *head;

	while (temp)
	{
		len++;
		temp = temp->next;
	}
	return (len);
}
