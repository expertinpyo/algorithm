#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


vector<int> vValue(1001);

void search(int day, int work)
{
	if (day <= 0)
		return;

	if (vValue[day] == 0)
		vValue[day] = work;

	else if (vValue[day] < work)
	{
		int prevValue = vValue[day];
		vValue[day] = work;
		search(day - 1, prevValue);
	}

	else if (vValue[day] >= work)
		search(day - 1, work);
	
	return;
}


bool compare(pair<int, int> p1, pair<int, int> p2)
{
	return p1.second > p2.second;
}

int main()
{
	int N;

	cin >> N;

	vector<pair<int, int>> vAssignment(N);

	for (int i = 0; i < N; i++)
	{
		int d, w;
		cin >> d >> w;
		vAssignment[i] = make_pair(d, w);
	}

	sort(vAssignment.begin(), vAssignment.end(), compare);
	
	int ans = 0;
	
	
	for (auto iter = vAssignment.begin(); iter != vAssignment.end(); iter++)
		search(iter->first, iter->second);

	for (auto iter = vValue.begin(); iter != vValue.end(); iter++)
		ans += *iter;

	cout << ans;
	
}