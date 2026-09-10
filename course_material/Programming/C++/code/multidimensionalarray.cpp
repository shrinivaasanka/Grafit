#include <array>
#include <iostream>

using namespace std;

template<typename T,std::size_t x,std::size_t y,std::size_t z>
class ndarray {
	std::array<T,x*y*z> multidimdata{};

public:
	T& operator[](this auto& self,std::size_t X,std::size_t Y,std::size_t Z)
	{
		return self.multidimdata[Z*Y*X + Y*X + X];
	}
};

int main()
{
	ndarray<int,5,5,5> multidim;
        for(auto i=0; i < 5; i++)
	{
        	for(auto j=0; j < 5; j++)
		{
        		for(auto k=0; k < 5; k++)
			{
				multidim[i,j,k]=i*j*k;
				cout<<"Multidimensional array element at index ["<<i<<","<<j<<","<<k<<"]:"<<multidim[i,j,k]<<endl;
			}
		}
	}
}

