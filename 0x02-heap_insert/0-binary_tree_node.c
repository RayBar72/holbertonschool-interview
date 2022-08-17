#include "binary_trees.h"



binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *son = NULL;

	son = malloc(sizeof(*son));
	if (!son)
		return (NULL);
	son->parent = parent;
	son->n = value;
	return (son);
}
