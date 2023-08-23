#include "regex.h"

/**
 * regex_match - checks if a regex matchs to string
 * @s: sing to be searched
 * @p: regex
 * Return: 1 if match, else 0
*/

int regex_match(char const *s, char const *p)
{
	if (!*s)
		return (!*p || (p[1] == '*' && regex_match(s, p + 2)));
	if (p[1] == '*')
		return ((*p == '.' || *s == *p) ? (regex_match(s + 1, p) || 
				regex_match(s, p + 2)) : (regex_match(s, p + 2)));
	return ((*p == '.' || *p == *s) && regex_match(s + 1, p + 1));
}
