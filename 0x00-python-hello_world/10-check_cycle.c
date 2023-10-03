#include"lists.h"
/**
 * check_cycle - Checks if a linked list has a cycle
 *
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if a cycle is found, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list, *nextptr;
	while(head)
	{
		nextptr = head->next;
		while(nextptr)
		{
			if (nextptr == head)
				return (1);
			nextptr = nextptr->next;
		}
		head = head->next;
	}
	return (0);
}
