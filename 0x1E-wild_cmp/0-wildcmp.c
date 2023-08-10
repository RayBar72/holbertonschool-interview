#include "holberton.h"

/**
 * wildcmp - unction that compares two strings and returns 1
 * if the strings can be considered identical, otherwise return 0.
 * @s1: pointer to haystack string
 * @s2: pointer to the need string
 * Return: 1 if found other wise 0
*/

int wildcmp(char *s1, char *s2)
{
	if (!*s1)
	{
		if (*s2 == '*')
			return (wildcmp(s1, s2 + 1));
		return (!*s2);
	}
	if (*s2 == '*')
		return (wildcmp(s1 + 1, s2) || wildcmp(s1, s2 + 1));
	if (*s1 != *s2)
		return (0);
	return (wildcmp(s1 + 1, s2 + 1));
}
