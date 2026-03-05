#include <algorithm>
#include <iostream>
#include <array>
#include <cmath>

using namespace std;

int main(int argc, char* argv[])
{
	const int num_to_factorize = std::atoi(argv[1]);
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
