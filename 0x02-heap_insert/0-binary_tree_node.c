#include "binary_trees.h"

/**
 * binary_tree_node - function that creates a node of binary tree
 * @parent: pointer to parent node
 * @value: value to be in node
 * Return: pointer to new node o NULL
 */

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *son = NULL;

	son = malloc(sizeof(*son));
	if (!son)
		return (NULL);
	memset(son, 0, sizeof(*son));
	son->parent = parent;
	son->n = value;
	return (son);
}
