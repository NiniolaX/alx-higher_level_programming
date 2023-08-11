#include "lists.h"
#include <unistd.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Head of list
 * Return: 0 if there is no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	if (list == NULL)
		return (0);

	/* Pointer to move in steps of one */
	ptr1 = list;
	/* Pointer to move in steps of two */
	ptr2 = list;

	while (ptr2 != NULL && ptr2->next != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr2 == ptr1)
			return (1);
	}
	/* Loop terminates indicating no cycle */
	return (0);
}
