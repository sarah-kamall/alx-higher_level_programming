#include<stdlib.h>
#include <stddef.h>
#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *head0, *head1, *prev = NULL, *it;

	head0 = *head;
	it = *head;
	while(head0)
	{
		head1 = malloc(sizeof(listint_t));
		if (!head1)
			free_listint(head1);
		head1-> n = head0->n;
		head1->next = prev;
		prev = head1;
		head0 = head0->next;
	}
	while(it)
	{
		if (it->n != head1->n)
		{
			free_listint(head1);
			return (0);
		}
		else
		{
			it = it->next;
			head1 = head1->next;
		}
	}
	free_listint(head1);
	return (1);
}

		
