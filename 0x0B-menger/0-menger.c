#include "menger.h"

/**
 * menger_1 - Function that prints menger
 * @level: int with the number of levels
 */

static void menger_1(int level)
{
	int i = 0, j = 0, _i = 0, _j = 0, c;

	for (i = 0; i < level; i++)
	{
		for (j = 0; j < level; j++)
		{
			_i = i;
			_j = j;
			c = '#';
			while (_i || _j)
			{
				if (_i % 3 == 1 && _j % 3 == 1)
				{
					c = ' ';
				}
				_i /= 3;
				_j /= 3;
			}
			putchar(c);
		}
		putchar('\n');
	}
}

/**
 * menger - Function that prints menger
 * @level: int with the number of levels
 */

void menger(int level)
{
	double counter = 0;

	if (level < 0)
		exit(0);
	else if (level == 0)
		printf("#\n");
	else if (level >= 1)
	{
		counter = pow(3, (level));
		menger_1(counter);
	}
}
