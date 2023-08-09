#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted linked list
 * @head: Address of head node of list
 * @number: Number to be inserted
 * Return: Address of new node on success, NULL on fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new;

	/* Check that valid address is passed */
	if (head == NULL)
		return (NULL);
	ptr = *head;

	/* Build new node */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	/* Add new node if list is empty */
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	/* If list is not empty */
	if (number < 0 && ptr->n >= 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (ptr->next != NULL && number > (ptr->next)->n)
		ptr = ptr->next;
	new->next = ptr->next;
	ptr->next = new;

	return (new);
}
