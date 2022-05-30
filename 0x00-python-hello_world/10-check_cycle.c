#include "lists.h"

/**
 * check_cycle - detects a cycle in a linked list
 * @list: a list
 * Return: 1 if htere is a cycle and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *list1, *list2;

	list1 = list;
	list2 = list;

	while (list1 && list2 && list2->next)
	{
		list1 = list1->next;
		list2 = list2->next->next;
		if (list1 == list2)
			return (1);
	}
	return (0);
}
