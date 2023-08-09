#include "lists.h"
#include <unistd.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Head of list
 * Return: 0 if there is no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *temp;

	if (list == NULL)
	{
		write(STDERR_FILENO, "Empty list", 11);
		return (0);
	}
	ptr = list;
	temp = list;

	while (ptr->next)
	{
		/* ptr hits a previously traversed head node */
		if (ptr->next == temp)
			return (1);
		ptr = ptr->next;
	}
	/* Loop terminates indicating no cycle */
	return (0);
}
