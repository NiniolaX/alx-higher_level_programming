#include "lists.h"

/**
 * insert_node - Inserts a node into a singly linked list
 * @head: Address of head node
 * @number: Interger element of new node
 * Return: New node on sucess, NULL on fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new;

	if (head == NULL)
		return (NULL);
	ptr = *head;

	/* Build the new node */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	/* If list is empty*/
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	/* If number is negative & less than head node element */
	if (number < 0 && number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	/* If list is not empty */
	while (ptr->next != NULL && (ptr->next)->n < number)
		ptr = ptr->next;

	new->next = ptr->next;
	ptr->next = new;

	return (new);
}
