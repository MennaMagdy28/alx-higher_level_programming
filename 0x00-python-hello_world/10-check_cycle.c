#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has cycle in it
 * @list: pointer
 * Return: 0, 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *p;

	temp = list;
	p = list;
	while (list && temp && temp->next)
	{
		list = list->next;
		temp = temp->next->next;

		if (list == temp)
		{
			list = p;
			p =  temp;
			while (1)
			{
				temp = p;
				while (temp->next != list && temp->next != p)
				{
					temp = temp->next;
				}
				if (temp->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}