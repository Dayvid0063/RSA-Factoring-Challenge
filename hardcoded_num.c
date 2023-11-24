#include <stdio.h>

int main()
{
	long long int digits = 239809320265259;
	long int elem1, elem2;

	elem1 = 2;

	while (digits % elem1)
	{
		if (elem1 <= digits)
		{
			elem1++;
		}
		else {
			return (-1);
		}
	}

	elem2 = digits / elem1;
	printf("%lld = %ld * %ld\n", digits, elem2, elem1);
	return (0);
}
