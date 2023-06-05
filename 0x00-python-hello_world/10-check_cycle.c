#include "lists.h"

/**
 * check_cycle -  This function checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *new = list;
	listint_t *prev = new;

	while (new && prev && new->next)
	{
		prev = prev->next;
		new = new->next->next;
		if (prev == new)
			return (1);
	}
	return 0;
}
