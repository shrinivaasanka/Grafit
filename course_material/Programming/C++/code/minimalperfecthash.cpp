#include <iostream>
#include <array>

using namespace std;
std::array<int,20> mphf;
void store_in_mphf(std::array<int,20>&);
bool find_element_in_mphf(int);

int main()
{
	std::array<int,20> array={1,2,3,4,8,0,5,6,7,9,11,12,13,14,15,10,19,18,17,16};
	store_in_mphf(array);
	int ret1=find_element_in_mphf(3);
	int ret2=find_element_in_mphf(25);
	int ret3=find_element_in_mphf(105);
	int ret4=find_element_in_mphf(15);
}

void store_in_mphf(std::array<int,20>& array)
{
	cout<<"size of mphf:"<<mphf.size()<<endl;
	for(int i=0;i <= mphf.size();i++)
	{
		mphf[i]=-1;
	}
	for(auto n:mphf)
	{
		cout<<"Before update:mphf contains:"<<n<<endl;
	}
	int k=0;
	for(auto x:array)
	{
		mphf[array[k++]]=x;
	}
	for(auto n:mphf)
	{
		cout<<"After update:mphf contains:"<<n<<endl;
	}
}

bool find_element_in_mphf(int element)
{
	cout<<"mphf["<<element<<"] == "<<mphf[element]<<endl;
	if (mphf[element] != element)
	{
		cout<<"Element "<<element<<" does not exist in mphf"<<endl; 
		return false;
	}
	else
	{
		cout<<"Element "<<element<<" exists in mphf"<<endl; 
		return true;	
	}
}
