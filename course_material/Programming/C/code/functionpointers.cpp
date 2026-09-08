#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int* function1();
float* function2();
void* (*fp)();

int main()
{
	srand(time(NULL));
	int randint;
	int iterations=0;
	while(iterations++ <= 10)
	{
		randint=rand()%2;
		printf("Random integer:%d\n",randint);
		switch(randint)
		{
			case 0:
				fp=(void* (*)())function1;
				break;
			case 1:
				fp=(void* (*)())function2;
		}
		void* ret=(*fp)();
		if(randint==0)
			printf("Returned value: %d\n",*(int*)ret);
		else
			printf("Returned value: %f\n",*(float*)ret);
	}
}

int* function1()
{
	int* ret=(int*)malloc(sizeof(int));
	printf("function1() returning int\n");
	*ret=100;
	return ret;
}

float* function2()
{
	float* ret=(float*)malloc(sizeof(float));
	printf("function2() returning float\n");
	*ret=10.0;
	return ret;
}
