#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is palindrome
 * @head: Address of head node
 * Return: 0 if list is not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *current, *next, *first, *second;

	/* Address is NULL or list is empty */
	if (head == NULL || *head == NULL)
		return (1);

	/* Move slow ptr to centre of list */
	slow = *head;
	fast = *head;
	while (fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	/* Reverse second half of list */
	prev = NULL;
	current = slow->next;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	/* Compare first half of list with reversed second half */
	first = *head;
	second = prev;
	while (second != NULL)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = second->next;
	}
	return (1);
}
