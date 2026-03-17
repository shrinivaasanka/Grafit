#include <cmath>
#include <iostream>

using namespace std;
long double factorial(int x);

int ramanujan_pi(int maxrange);
int chudnovsky_pi(int maxrange);

int main(int argc,char* argv[])
{
	int maxrange=atoi(argv[1]);
	ramanujan_pi(maxrange);
	chudnovsky_pi(maxrange);
}

int ramanujan_pi(int maxrange)
{
	long double approximatepi1=0;
	long double approximatepi2=0;
	approximatepi1=2*std::sqrt(2)/9801;
	for(int n=0;n < maxrange;n++)
	{
		long double seriesterm1 = factorial(4*n)*(1103+26390*n);
		cout<<"seriesterm1:"<<seriesterm1<<endl;
		long double seriesterm2 = std::pow(factorial(n),4)*std::pow(396,4*n);
		cout<<"seriesterm2:"<<seriesterm2<<endl;
		approximatepi2 += (seriesterm1/seriesterm2);
		cout<<"Approximate value of Pi (Ramanujan's series):"<<1/(approximatepi1*approximatepi2)<<endl;
	}
	cout<<"Approximate value of Pi (Ramanujan's series):"<<1/(approximatepi1*approximatepi2)<<endl;
}

int chudnovsky_pi(int maxrange)
{
	long double approximatepi1=0;
	long double approximatepi2=0;
	approximatepi1=1/(426880*std::sqrt(10005));
	for(int n=0;n < maxrange;n++)
	{
		long double seriesterm1 = factorial(6*n)*(13591409+545140134*n);
		cout<<"seriesterm1:"<<seriesterm1<<endl;
		long double seriesterm2 = factorial(3*n)*std::pow(factorial(n),3)*std::pow(-1*640320,3*n);
		cout<<"seriesterm2:"<<seriesterm2<<endl;
		approximatepi2 += (seriesterm1/seriesterm2);
		cout<<"Approximate value of Pi (Chudnovsky brothers variant of Ramanujan's series):"<<1/(approximatepi1*approximatepi2)<<endl;
	}
	cout<<"Approximate value of Pi (Chudnovsky brothers variant of Ramanujan's series):"<<1/(approximatepi1*approximatepi2)<<endl;
}

long double factorial(int x)
{
	long double ret=x;
	//cout<<"factorial(): ret:"<<ret<<endl;
	if(ret==0)
	{
		return 1;
	}
	return ret*factorial(x-1);
}
