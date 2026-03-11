#include <algorithm>
#include <iostream>
#include <array>
#include <cmath>
#include <chrono>

using namespace std;

void factorization1(int& num_to_factorize);
void factorization2(int& num_to_factorize);

int main(int argc, char* argv[])
{
	int num_to_factorize = std::atoi(argv[1]);
	cout<<"-------------------------------------------------"<<endl;
	cout<<"1.Factorization1 - Exhaustive real plane search"<<endl;
	cout<<"-------------------------------------------------"<<endl;
	auto start = std::chrono::high_resolution_clock::now();
	factorization1(num_to_factorize);
	auto end = std::chrono::high_resolution_clock::now();
	auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end-start).count();
	cout<<"1.Bruteforce factorization1() - exhaustive real plane search -  runtime in nanoseconds:"<<duration<<endl;
	cout<<"-------------------------------------------------"<<endl;
	cout<<"2.Factorization2 - Recursive trial division"<<endl;
	cout<<"-------------------------------------------------"<<endl;
	start = std::chrono::high_resolution_clock::now();
	factorization2(num_to_factorize);
	end = std::chrono::high_resolution_clock::now();
	duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end-start).count();
	cout<<"2.Bruteforce factorization2() - recursive trial division - runtime in nanoseconds:"<<duration<<endl;
}

void factorization1(int& num_to_factorize)
{
	int exponent;
	for(int x=1;x <= num_to_factorize;x++)
	{
		double factorcandidate = double(num_to_factorize)/double(x);
		cout<<"factorcandidate:"<<factorcandidate<<endl;
		double decimal = fmod(factorcandidate,1.0);
		cout<<"decimal:"<<decimal<<endl;
		if(decimal==0.0) 
		{
			cout<<"---------------------------------------------------------------"<<endl;
			cout<<"Factors of "<<num_to_factorize<<" are "<<factorcandidate<<" and "<<x<<endl;
			cout<<"---------------------------------------------------------------"<<endl;
		}
	}
}

void factorization2(int& num_to_factorize)
{
	int integer=num_to_factorize;
	for(int x=1;x <= num_to_factorize;x++)
	{
		int remainder = integer%x;
		if(remainder == 0)
		{
			cout<<"Factor of "<<num_to_factorize<<" found:"<<x<<endl;
			integer = integer/x;
		}
	}
}
