#include "slide_line.h"

/**
 * zero_move - function that moves zeros over the int array
 * @line: array to be orderer
 * @size: size of array line
 * @direction: left or right side to be changed numbers
 */

static void zero_move(int *line, size_t size, int direction)
{
size_t i = 0;

	if (direction == SLIDE_LEFT)
	{
		while (i < size - 1)
		{
			if (line[i] == 0 && line[i + 1] != 0)
			{
				line[i] = line[i + 1];
				line[i + 1] = 0;
			}
			i++;
		}
	}
	else
	{
		i = size - 1;
		while (i)
		{
			if (line[i] == 0 && line[i - 1] != 0)
			{
				line[i] = line[i - 1];
				line[i - 1] = 0;
			}
			i--;
		}
	}
}

/**
 * sum_game - function that moves zeros over the int array
 * @line: array to be orderer
 * @size: size of array line
 * @direction: left or right side to be changed numbers
 */

static void sum_game(int *line, size_t size, int direction)
{
size_t i = 0;
int a = 0;

	if (direction == SLIDE_LEFT)
	{
		while (i < size - 1)
		{
			if (line[i] == line[i + 1])
			{
				a = line[i];
				line[i] = line[i + 1] + a;
				line[i + 1] = 0;
			}
			i++;
		}
	}
	else
	{
		i = size - 1;
		while (i)
		{
			if (line[i] == line[i - 1])
			{
				a = line[i];
				line[i] = line[i - 1] + a;
				line[i - 1] = 0;
			}
			i--;
		}
	}
}

/**
 * slide_line - function that moves zeros over the int array
 * @line: array to be orderer
 * @size: size of array line
 * @direction: left or right side to be changed numbers
 * Return: 1 if success, 0 other case
 */

int slide_line(int *line, size_t size, int direction)
{
	size_t i = 0;

	if (direction == SLIDE_LEFT || direction == SLIDE_RIGHT)
	{
		for (i = 0; i < size; i++)
			zero_move(line, size, direction);
		sum_game(line, size, direction);
		for (i = 0; i < size; i++)
			zero_move(line, size, direction);
		return (1);
	}
	else
		return (0);
}
