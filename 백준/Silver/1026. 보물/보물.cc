#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int main()
{
	// B의 순서에 맞게 A를 배치시켜야 함

	int n;
	cin >> n;
	
	vector<int> arrA(n);
	vector<pair<int, int>> arrB;

	for (int i = 0; i < n; i++)
		cin >> arrA[i];
	
	for (int i = 0; i < n; i++)
	{
		int temp;
		cin >> temp;

		arrB.emplace_back(make_pair(temp, i));
	}

	sort(arrB.begin(), arrB.end());
	sort(arrA.begin(), arrA.end());
	
	int ans = 0;


	for (int i = 0; i < n; i++)
	{
		ans += ( arrB[i].first * arrA[n - 1 - i]);
	}
	
	cout << ans;

}