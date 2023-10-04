#include"lists.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *nextq, *new;
	if (*head)
	{
		prev = *head;
		nextq = (*head)->next;
		while (nextq && nextq->n < number)
		{
			nextq = nextq->next;
			prev = prev->next;
		}
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
		new->n = number;
		new->next = nextq;
		prev->next = new;
		return (new);
	}
	else
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);
	}
	return (NULL);
}

