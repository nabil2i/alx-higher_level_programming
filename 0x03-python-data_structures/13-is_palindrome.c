#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: list
 * Return: 0 if it is not a palindrome
 *	1 otherwise
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *cursor;
	int count, i, j;

	cursor = *head;
	count = 1;

	while (cursor->next)
	{
		cursor = cursor->next;
		count++;
	}
	int data[count];

	cursor = *head;
	i = 0;
	while (i < count)
	{
		data[i] = cursor->n;
		i++;
		cursor = cursor->next;
	}
	for (i = 0, j = count - 1; i <  count / 2; i++, j--)
	{
		if (data[i] != data[j])
		{
			return (0);
		}
	}
	return (1);
}
