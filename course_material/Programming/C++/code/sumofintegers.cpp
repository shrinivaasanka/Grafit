#include <iostream>
#include <vector>

using namespace std;

int main()
{
	std::vector<int> number1;
	std::vector<int> number2;
	std::vector<int> number3;
	int digit=0;
	std::cout<<"Number 1"<<endl;
	do
	{
		std::cin>>digit;
		std::cout<<"digit read:"<<digit<<endl;
		number1.push_back(digit);
	}
	while(digit != -1);
	std::cout<<"Number 2"<<endl;
	do
	{
		std::cin>>digit;
		std::cout<<"digit read:"<<digit<<endl;
		number2.push_back(digit);
	}
	while(digit != -1);
	std::cout<<"Number 1 (as vector)"<<endl;
	for(auto it3=number1.begin();*it3 != -1;it3++)
		std::cout<<*it3;
	std::cout<<endl;
	std::cout<<"Number 2 (as vector)"<<endl;
	for(auto it3=number2.begin();*it3 != -1;it3++)
		std::cout<<*it3;
	std::cout<<endl;
	int carry=0;
	for(int index=number1.size()-2;index >= 0;index--)
	{
		cout<<"Number1 - digit:"<<number1.at(index)<<endl;
		cout<<"Number2 - digit:"<<number2.at(index)<<endl;
		digit=(number1.at(index) + number2.at(index) + carry)%10;
		cout<<"Number3 - digit:"<<digit<<endl;
		carry=(number1.at(index) + number2.at(index) + carry)/10;	
		cout<<"Number3 - carry:"<<carry<<endl;
		number3.push_back(digit);
	}
	number3.push_back(carry);
	std::cout<<"Sum of 2 integer vectors - Number1 and Number2:"<<endl;
	for(int index=number3.size()-1;index >= 0;index--)
		std::cout<<number3.at(index);
	std::cout<<endl;
}

