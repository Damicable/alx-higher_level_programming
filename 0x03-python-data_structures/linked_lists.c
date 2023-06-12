#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - This is a function that prints all elements of a listint_t list
 * @h: A pointer to head of list
 * Return: number of nodes
 */

size_t print_listint(const listint_t *h)
{
	const listint_t *orig;
	unsigned int n; /* number of nodes */

	orig = h;
	n = 0;
	while (orig!= NULL)
	{
		printf("%i\n", orig->n);
		orig = orig->next;
		n++;
	}

	return (n);
}

}

/**
 * add_nodeint_end - This adds a new node at the end of a listint_t list
 * @head: pointer that points to first node of listint_t list
 * @n: Integer to be included in new node
 * Return: Address of the new element or NULL if it fails
 */

listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *orig;

	orig = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (orig->next != NULL)
			orig = orig->next;
		orig->next = new;
	}
	
	return (new);
}

/**
 * free_listint - This function frees a listint_t list
 * @head: A pointer to list to be freed
 * Return: void
 */

void free_listint(listint_t *head)
{
	listint_t *orig;
	
	while (head != NULL)
	{
		orig = head;
		head = head->next;
		free(orig);
	}
}
