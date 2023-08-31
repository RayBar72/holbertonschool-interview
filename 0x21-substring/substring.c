#include "substring.h"

#define INDICE(x) ((x) - 'a')

/**
 * free_srch - frees nodes of srch
 * @root: pointer
 */
void free_srch(srch *root)
{
	int i = 0;

	for (i = 0; i < 26; i++)
		if (root->son[i])
			free_srch(root->son[i]);
	free(root);
}

/**
 * search_srch - searches for word
 * @node: first node of tree
 * @str: to be finded
 * @k: characters of str to find
 * @memo: the memoization array
 * @j: index in memo
 * Return: 1 if found else 0
 */
int search_srch(srch *node, char *str, int k, srch **memo, int j)
{
	for (; k; str++, k--)
	{
		if (!node->son[INDICE(*str)])
			return (0);
		node = node->son[INDICE(*str)];
	}

	memo[j] = node;
	if (node->left-- > 0)
	{
		return (1);
	}
	return (0);
}

/**
 * make_srch - fills search with words
 * @root: root of search
 * @words: pointer to array
 * @nb_words: number of words
 * @nodes: array of srch nodes to populate
 */
void make_srch(srch *root, char const **words, int nb_words, srch **nodes)
{
	int i = 0;
	char const *str;
	srch *node;

	for (i = 0; i < nb_words; i++)
	{
		node = root;
		for (str = words[i]; *str; str++)
		{
			if (!node->son[INDICE(*str)])
			{
				node->son[INDICE(*str)] = calloc(1, sizeof(srch));
				if (!node->son[INDICE(*str)])
					exit(1);
			}
			node = node->son[INDICE(*str)];
		}
		node->word = 1;
		node->count++;
		node->left++;
		node->val = (char *)words[i];
		nodes[i] = node;
	}
}
/**
 * find_substring - finds substring composed of all concatenated words
 * @s: string to search
 * @words: contentated words to find
 * @nb_words: size of array
 * @n: size of return array, to set
 * Return: array of indices where all words found
 */
int *find_substring(char const *s, char const **words, int nb_words, int *n)
{
	int i = 0, j, k, slen, matches;
	srch *root, **nodes, **memo;
	int *indices;

	*n = 0;
	slen = strlen(s);
	k = strlen(words[0]);
	indices = calloc(slen, sizeof(int));
	root = calloc(1, sizeof(srch));
	nodes = calloc(nb_words, sizeof(*nodes));
	memo = calloc(slen, sizeof(*memo));
	if (!indices || !root || !nodes || !memo)
		exit(1);
	make_srch(root, words, nb_words, nodes);

	for (i = 0; i < slen; i++)
	{
		matches = 0;
		for (j = i; j <= slen - k; j += k)
		{
			if ((memo[j] && memo[j]->left-- > 0) ||
				search_srch(root, (char *)s + j, k, memo, j))
			{
				if (++matches == nb_words)
				{
					indices[*n] = i;
					*n += 1;
					break;
				}
			}
			else
				break;
		}
		for (j = 0; j < nb_words; j++)
			nodes[j]->left = nodes[j]->count;
	}
	free_srch(root), free(nodes), free(memo);
	if (*n == 0)
		indices = (free(indices), NULL);
	return (indices);
}
