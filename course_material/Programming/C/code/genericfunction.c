#include <stdio.h>
#include <stdlib.h>
#include <string.h>

union generic
{
	int integer;
	float real;
        char* string;
};	

void* function1(int datatype);
generic function2(int datatype);

int main()
{
	/*********** Union ***********/
	union generic Generic;
	int var1 = function2(1).integer;
	printf("Union - var1 = %d\n",var1);
	float var2 = function2(2).real;
	printf("Union - var2 = %f\n",var2);
	char* var3 = function2(3).string;
	printf("Union - var3 = %s\n",var3);
	/************ Void pointer ********/
	var1 = *((int*)function1(1));
	printf("Void* - var1 = %d\n",var1);
	var2 = *((float*)function1(2));
	printf("Void* - var2 = %f\n",var2);
	var3 = (char*)function1(3);
	printf("Void* - var3 = %s\n",var3);
}

generic function2(int datatype)
{
	generic* g=(generic*)malloc(sizeof(generic));
	switch(datatype)
	{
		case 1:
			g->integer=100;
			return *g;
		case 2:
			g->real=200.0;
			return *g;
		case 3:
			g->string="string";
			return *g;
	}
}

void* function1(int datatype)
{
	int* variable1=(int*)malloc(sizeof(int));
	float* variable2=(float*)malloc(sizeof(int));
	char* variable3=(char*)malloc(sizeof(char)*10);
	strcpy(variable3,"string");
	switch(datatype)
	{
		case 1:
			*variable1=100;
			//printf("variable1=%d\n",*variable1);
			return variable1;
		case 2:
			*variable2=200;
			//printf("variable2=%f\n",*variable2);
			return variable2;
		case 3:
			return variable3;	
	}
}
