#include "menger.h"

void menger_1(int level)
{
	int i = 0, j = 0;

	for (i = 0; i <= level; i++)
	{	
		for (j = 0; j <= level; j++)
		{
			printf("###");
		}
		putchar(10);
		for (j = 0; j <= level; j++)
		{
			printf("# #");
		}
		putchar(10);
		for (j = 0; j <= level; j++)
		{
			printf("###");
		}
		putchar(10);
	}
}

void menger(int level)
{
	double counter = 0;

	if (level < 0)
		exit(0);
	else if (level == 0)
		printf("#\n");
	else if (level >= 1)
	{
		counter = pow(3, (level - 1));
		menger_1(counter);
	}
}
