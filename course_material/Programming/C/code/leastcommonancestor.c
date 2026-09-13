#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node 
{
	int data;
	struct node* left;
	struct node* right;
	struct node* parent;
};

int find_least_common_ancestor(struct node* nodex, struct node* nodey);

int main()
{
	struct node root;
	struct node node1,node2,node3,node4,node5;
	root.left=&node1;
	root.right=&node2;
	root.data=0;
	node1.data=1;
	node2.data=2;
	node1.parent=&root;
	node2.parent=&root;
	node1.left=&node3;
	node3.parent=&node1;
	node3.data=3;
	node2.right=&node4;
	node4.parent=&node2;
	node4.left=&node5;
	node5.parent=&node4;
	node4.data=4;
	node5.data=5;
	find_least_common_ancestor(&node3,&node5);
}

int in_ancestors1(int* ancestors1,int num_ancestors1,int data)
{
	for(int i=0;i < num_ancestors1;i++)
	{
		if(data == ancestors1[i])
		{
			printf("Ancestor matched between nodex and nodey\n");
			return 1;
		}
	}
	printf("Ancestor didnot match between nodex and nodey\n");
	return 0;

}

int find_least_common_ancestor(struct node* nodex,struct node* nodey)
{
	struct node* temp1=nodex;
	struct node* temp2=nodey;
	int n=0;
	int m=0;
	int *ancestors1=(int*)malloc(sizeof(int)*100);
	while(temp1 != NULL)
	{
		printf("going up tree from nodex...level:%d\n",n);
		printf("Creating ancestors for nodex ....\n");
		ancestors1[n++]=temp1->data;
		temp1=temp1->parent;
	}
	while(temp2 != NULL)
	{
		printf("going up tree from nodey...level:%d\n",m);
		printf("Looking up nodey ancestor in nodex ancestors....\n");
		if(in_ancestors1(ancestors1,n,temp2->data))
			printf("Found least common ancestor:%d\n",temp2->data);
		temp2=temp2->parent;
		m++;
	}
}
