#include "lists.h"

/**
 * insert_node - This is a function that inserts a number into a sorted singly-linked list.
 * @head: Pointer the head of the linked list.
 * @number: Number to insert.
 * Return: NULL if the function fails otherwise, pointer to the current node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *current;

	current = malloc(sizeof(listint_t));
	if (current == NULL)
		return (NULL);
	current->n = number;

	if (node == NULL || node->n >= number)
	{
		current->next = node;
		*head = current;
		return (current);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	current->next = node->next;
	node->next = current;

	return (current);
}
