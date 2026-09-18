#include <vector>
#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;
struct node
{
	int bit; 
	struct node* left;
	struct node* right;
	node() 
	{
		bit=0;
		left=NULL;
		right=NULL;
	}
};

void print_trie(struct node* root)
{
	if(root != NULL)
	{
		cout<<"Node data: "<<root->bit<<endl;
		cout<<"Traversing left subtree..."<<endl;
		print_trie(root->left);
		cout<<"Traversing right subtree..."<<endl;
		print_trie(root->right);
	}
	return;
}

int insert_into_trie(int integer, int maxintlen, struct node* root)
{
	std::vector<int> bitsinsertedsofar;
	struct node* temp=root;
	int pos=0;
	cout<<"--------------- Inserting to Trie - integer "<<integer<<endl;
	while(pos <= maxintlen)
 	{
		int depth=pos;
		cout<<"depth:"<<depth<<endl;
		int presentbit = (integer >> pos) & 1; 
		printf("presentbit: %d\n",presentbit);
		for(int n:bitsinsertedsofar)
		{
			cout<<"========================================="<<endl;
			if(n == 0)
				temp=temp->left;
			if(n == 1)
				temp=temp->right;
			cout<<"bit on Trie:"<<temp->bit<<endl;
			cout<<"bit inserted so far:"<<n<<endl;
			cout<<"========================================="<<endl;
		}
		if(presentbit == 0)
		{
			if(temp->left == NULL)
			{
				temp->left = new node();
				temp->left->bit = presentbit;
				temp->left->left = NULL;
				temp->left->right = NULL;
				printf("presentbit is 0, Inserting a new node to left ...\n");
			}
		}
		if(presentbit == 1)	
		{
			if(temp->right == NULL)
			{
				temp->right = new node();
				temp->right->bit = presentbit;
				temp->right->left = NULL;
				temp->right->right = NULL;
				printf("presentbit is 1, Inserting a new node to right...\n");
			}
		}
		bitsinsertedsofar.push_back(presentbit);
		pos++;
		temp=root;
	}
	return 1;
}

int main()
{
	struct node trie_root;
	trie_root.bit=0;
	trie_root.left=NULL;
	trie_root.right=NULL;
	insert_into_trie(5,3,&trie_root);
	insert_into_trie(2,3,&trie_root);
	insert_into_trie(3,3,&trie_root);
	insert_into_trie(4,3,&trie_root);
	insert_into_trie(7,3,&trie_root);
	cout<<"------ printing Trie ---------- "<<endl;
	print_trie(&trie_root);
}
