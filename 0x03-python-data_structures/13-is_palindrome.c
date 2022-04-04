/*#include "lists.h"*/
/*int check_palindrome(listint_t **left_ptr, listint_t *right_ptr);*/
/**
 * is_palindrome - C Function checks if single linked list is palindrome
 * @head: Head ptr of list to check
 *
 * Return: 1 if a palindrome 0 otherwise
 *
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_palindrome(head, *head));
}
**
 * check_palindrome - Utility to check if palindrome with recursion
 * @left_ptr: Pointer to left side of the list
 * @right_ptr: Pointer to right side of the list
 *
 * Return: 1 if a Palindrome 0 otherwise
 *
int check_palindrome(listint_t **left_ptr, listint_t *right_ptr)
{
	if (!right_ptr)
		return (1);
	if (check_palindrome(left_ptr, right_ptr->next)
			&& ((*left_ptr)->n == right_ptr->n))
	{
		(*left_ptr) = (*left_ptr)->next;
		return (1);
	}
	return (0);
}
*/
#include "lists.h"
#define IS_PALINDROME 1
#define NOT_PALINDROME 0

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: adress of the pointer to the head of the list
 *
 * Return: 1 if a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{

	if (!head)
		return (NOT_PALINDROME);
	if (!*head)
		return (IS_PALINDROME);

	return (is_palindrome_helper(*head, *head, (*head)->next));
}


int is_palindrome_helper(listint_t *h, listint_t *p_last, listint_t *forward)
{
	int result;

	if (!h)
		return (IS_PALINDROME);

	if (!forward)
		return (h->n == p_last->n);


	result = (is_palindrome_helper(h, forward, forward->next));



	return (is_palindrome_helper(h->next, p_last, forward) && result);
}
