#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct memblock
{
	void* startaddress;
	int size;
	struct memblock* nextblock;
};

static struct memblock *memblocklist=NULL;
static struct memblock *memblocklistbegin=NULL;
static int nextavailableindex=0;
void* memalloc(void* heap,int size);
void loopthrough(struct memblock* memblocklist);
int main()
{
	void* heap=malloc(1000);
	int* integer1=(int*)memalloc(heap,sizeof(int)*10);
	printf("integer1 allocated at: %p \n",integer1);
	double* integer2=(double*)memalloc(heap,sizeof(double)*10);
	printf("integer2 allocated at: %p \n",integer2);
	printf("integer2-integer1 address gap: %ld \n",(char*)integer2-(char*)integer1);
	char* string1=(char*)memalloc(heap,sizeof(char)*10);
	printf("string1 allocated at: %p \n",string1);
	printf("string1-integer2 address gap: %ld \n",(char*)string1-(char*)integer2);
	loopthrough(memblocklistbegin);
	fflush(stdout);
}

void loopthrough(struct memblock* memblocklist)
{
	printf("=============================================\n");
	while(memblocklist != NULL)
	{
		printf("block starts at: %p\n",memblocklist->startaddress);
		printf("block size: %d\n",memblocklist->size);
		printf("next block: %p \n",memblocklist->nextblock);
		memblocklist=memblocklist->nextblock;
	}
}

void* memalloc(void* heap,int size)
{
	void* bufferbegin=heap+nextavailableindex;
        void* bufferend=heap+nextavailableindex+size;	
	nextavailableindex+=size;
	if(memblocklist==NULL)
	{
		printf("First allocation from heap\n");
		memblocklist=(struct memblock*)malloc(sizeof(struct memblock));
		memblocklistbegin=memblocklist;
		memblocklist->startaddress=bufferbegin;
		memblocklist->size=size;
		memblocklist->nextblock=NULL;
	}
	else
	{
		printf("Next allocation from heap\n");
		memblocklist->nextblock=(struct memblock*)malloc(sizeof(struct memblock));
		memblocklist=memblocklist->nextblock;
		memblocklist->startaddress=bufferbegin;
		memblocklist->size=size;
		memblocklist->nextblock=NULL;
	}
	return bufferbegin;
}
