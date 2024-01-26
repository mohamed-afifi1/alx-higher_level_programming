#include "lists.h"
/**
* check_cycle - check if there is cycle linked list
* @list: pointer to linked list
*Return: 1 if cycle 0 if not cycle
**/
int check_cycle(listint_t *list)
{
	listint_t *f = list, *s = list;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
		return (1);
	}
	return (0);
}
