#include "binary_trees.h"

/**
 * node_number - function that returns the total num of nodes
 * @root: pointer to the root of the binary tree
 * Return: number of nodes in the tree
 */

static int node_number(heap_t *root)
{
	if (!root)
		return (0);
	return (1 + node_number(root->left) + node_number(root->right));
}

/**
 * node_height - Function that, based in node number,
 * calculates the height of a tree
 * @n: number of nodes
 * Return: height of the tree
 */

static int node_height(int n)
{
	int n2 = 0;

	while (1 << (n2 + 1) <= n)
	{
		n2++;
	}
	return (n2);
}

/**
 * heap_insert - function that insert a node in a heap
 * @root: pointer to the root node
 * @value: value to be inserted
 * Return: pointer or NULL
 */
heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *walker = *root, *retorno;
	int n = 0, h = 0;

	retorno = binary_tree_node(walker, value);
	if (!retorno)
		return (NULL);
	if (!*root)
		return (*root = retorno);
	n = node_number(*root) + 1;
	h = node_height(n);
	for (h--; h > 0; h--)
	{
		if (n & (1 << h))
			walker = walker->right;
		else
			walker = walker->left;
	}
	if (n & 1)
		walker->right = retorno;
	else
		walker->left = retorno;
	retorno->parent = walker;
	while (retorno && retorno->parent && retorno->n > retorno->parent->n)
	{
		retorno->parent->n = retorno->parent->n - retorno->n;
		retorno->n = retorno->parent->n + retorno->n;
		retorno->parent->n = retorno->n -  retorno->parent->n;
		retorno = retorno->parent;
	}
	return (retorno);
}
