#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly list.
 * @head: starting of the pointed node.
 * @number: numbers stored in the linked list.
 * Return: the address of the node,
 * otherwise return NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *new_node = NULL;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	
	if (
}
