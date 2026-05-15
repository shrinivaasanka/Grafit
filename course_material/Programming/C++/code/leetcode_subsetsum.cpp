#include <algorithm>
#include <vector>
#include <iostream>
#include <unordered_map>

class SubsetSum {
	public:
		std::vector<int> indices;
		std::unordered_map<int,int> sorted_to_unsorted_map;
		SubsetSum() { }
		void subsetsum_promise_approximation(std::vector<int>& integers, int expectedsum)
		{
			std::vector<int> sortedintegers(integers);
			std::sort(sortedintegers.begin(),sortedintegers.end());
			int n=0;
			for(auto it1 = sortedintegers.begin(); it1 != sortedintegers.end(); it1++)
			{
				auto it2 = std::find(integers.begin(),integers.end(),*it1);
				std::cout<<"it1:"<<*it1<<std::endl;
				std::cout<<"it2:"<<*it2<<std::endl;
				if (it2 != integers.end())
				{
					sorted_to_unsorted_map.insert({n,it2-integers.begin()});
				}
				n++;
			}
			for (auto kv: sorted_to_unsorted_map)
			{
				std::cout<<"k="<<kv.first<<";v="<<kv.second<<std::endl;
				std::cout<<"("<<sortedintegers[kv.first]<<" <===> "<<sortedintegers[kv.second]<<")"<<std::endl;
			}
			int sum=0;
			int i=0;
			for(auto it = sortedintegers.begin(); it != sortedintegers.end() ; it++)
			{
				sum += *it;
				indices.push_back(sorted_to_unsorted_map[i]);
				if (sum == expectedsum)
				{
					std::cout<<"Indices summing up to "<<expectedsum<<" in unsorted array"<<std::endl;
					break;
				}
				i++;
			}
			return;
		}
};

int main()
{
	SubsetSum ts;
	std::vector<int> integers = {10,5,8,7,6,1};
	ts.subsetsum_promise_approximation(integers,27);
	for(auto it = ts.indices.begin(); it != ts.indices.end(); it++)
	{
		std::cout<<"integer:"<<integers[*it]<<" at index "<<*it<<std::endl;
	}
}
