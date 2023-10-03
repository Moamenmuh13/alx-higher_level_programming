#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_list = list;
	listint_t *fast_list = list;

	while (slow_list != NULL && fast_list != NULL && fast_list->next != NULL)
	{
		slow_list = slow_list->next;
		fast_list = fast_list->next->next;

		if (slow_list == fast_list)
			return (1);
	}

	return (0);
}