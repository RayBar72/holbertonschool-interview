#include "palindrome.h"

/**
 * is_palindrome - Checks if unsigned integer is a palindrom
 * @n: number to be checked
 * Return: 1 if it is or 0 other wise
 */

int is_palindrome(unsigned long n)
{
	unsigned long c = 0, b = 0, d = 0;

	c = n;

	if (n < 10)
	{
		return (1);
	}
	else
	{
		while (c > 10)
		{
			b = c % 10;
			c /= 10;
			d = (d + b) * 10;
		}
		d += c;
		if (n == d)
		{
			return (1);
		}
		else
		{
			return (0);
		}
	}
}