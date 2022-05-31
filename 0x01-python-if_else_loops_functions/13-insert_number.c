#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly lined list
 * @head: list
 * @number: number to insert
 * Return: address of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cursor0, *cursor, *new;

	cursor = *head;
	cursor = *head;

	if (*head == NULL)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
		{
			return (NULL);
		}
		new->n = number;
		new->next = *head;
		*head = new;
		return (*head);
	}

	if (cursor->n > number) /* add at the front */
	{
		new = malloc(sizeof(listint_t));
		if (!new)
		{
			return (NULL);
		}
		else
		{
			new->n = number;
			new->next = (*head);
			*head = new;
			return (*head);
		}
	}

		while (cursor->next && cursor->n < number)
		{
			cursor0 = cursor;
			cursor = cursor->next;
		}
		if (!cursor->next) /* if we are at the end of the list */
		{
			new = malloc(sizeof(listint_t));
			if (!new)
			{
				return (NULL);
			}
			new->n = number;
			new->next = NULL;
			cursor->next = new;
			return (new);
		}
		else /* add at the middle of the list */
		{
			new = malloc(sizeof(listint_t));
			if (!new)
			{
				return (NULL);
			}
			new->n = number;
			new->next = cursor0->next;
			cursor0->next = new;
			return (new);
		}
}
