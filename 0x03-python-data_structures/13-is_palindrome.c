/*
 * File: 13-is_palindrome.c
 * Auth: Obidiegwu Ann
 */

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - This function reverses a singly-linked listint_t list.
 * @head: Pointer to the first node of the list to be reversed.
 *
 * Return: A pointer to the head of the reversed list.
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - This function checks if a singly linked list is a
 * palindrome or not.
 * @head: Is a pointer to the head of the linked list.
 *
 * Return: 0 if the linked list is not a palindrome otherwise, 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *prev;
	size_t size = 0, k;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (k = 0; k < (size / 2) - 1; k++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	prev = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&prev);

	return (1);
}
