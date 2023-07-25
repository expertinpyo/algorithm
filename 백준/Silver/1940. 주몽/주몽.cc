#include <iostream>
#include <vector>

using namespace std;


int main()
{
	int n, m;

	cin >> n;
	cin >> m;

	vector<int> arr;

	for (int i = 0; i < n; i++)
	{ 
		int input;
		cin >> input;
		arr.emplace_back(input);
	}

	auto iter1 = arr.begin();
	auto iter2 = iter1 + 1;
	
	int ans = 0;

	while (iter1 != arr.end())
	{
		if (iter2 == arr.end())
		{
			iter1++;
			iter2 = iter1 + 1;
			continue;
		}
		

		if (*iter1 + *iter2 == m)
		{
			ans++;
			iter2++;
			continue;
		}
		
		
		iter2++;
	}

	cout << ans;
}