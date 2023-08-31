#ifndef SUBSTRING_H
#define SUBSTRING_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *find_substring(char const *s, char const **words, int nb_words, int *n);

/**
 * struct srch - structure to search for words
 * @son: array for children nodes
 * @word: 1 if word, else 0
 * @count: number of words
 * @left: number of words at left
 * @val: point to the word
*/

typedef struct srch
{
	struct srch *son[26];
	int word;
	int count;
	int left;
	char *val;
} srch;


#endif
