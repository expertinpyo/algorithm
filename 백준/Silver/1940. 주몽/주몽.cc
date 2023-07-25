#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;

	cin >> n >> m;

	vector<int> arr(n, 0);

	for (int i = 0; i < n; i++)
	{ 
		cin >> arr[i];
	}

	sort(arr.begin(), arr.end());

	int left = 0;
	int right = n - 1;

	int ans = 0;

	while (left < right)
	{
		if (arr[left] + arr[right] < m)
			left++;
		else if (arr[left] + arr[right] > m)
			right--;
		else
		{
			ans++;
			left++;
			right--;
		}
	}

	cout << ans;
}
