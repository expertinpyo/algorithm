#include<iostream>
#include<algorithm>
#include<vector>


using namespace std;

vector<int> vPlus;
vector<int> vMinus;

int n, m;

bool compare(int a, int b)
{
	return a > b;
}

int calculation(vector<int>& vTemp)
{
	int idx = vTemp.size() - 1;
	int result = 0;
	int cnt = 1;

	while (idx >= 0)
	{
		if (idx < 0)
			break;
		if (cnt > m)
		{
			cnt = 1;
			continue;
		}
		if (cnt == 1)
			result += vTemp[idx] * 2;
		idx--;
		cnt++;

	}
	
	return abs(result);
}


int main(int argc, char** argv)
{
	cin >> n >> m;
	vector<int> vBook(n);

	for (int i = 0; i < n; i++)
	{
		cin >> vBook[i];

		if (vBook[i] > 0)
			vPlus.push_back(vBook[i]);
		else
			vMinus.push_back(vBook[i]);
	}
	
	sort(vPlus.begin(), vPlus.end());
	sort(vMinus.begin(), vMinus.end(), compare);

	int nSizePlus = vPlus.size();
	int nSizeMinus = vMinus.size();

	int ans = 0;

	if (nSizePlus && nSizeMinus)
	{
		// 양수, 음수 모두 있을 때
		ans += calculation(vPlus);
		ans += calculation(vMinus);

		if (vPlus.back() < abs(vMinus.back()))
			ans += vMinus.back();
		else
			ans -= vPlus.back();
	}
	else if (nSizePlus)
	{
		// 양수만 있을 떄
		ans += calculation(vPlus);
		ans -= vPlus.back();
	}
	else if (nSizeMinus)
	{
		// 음수만 있을 떄
		ans += calculation(vMinus);
		ans += vMinus.back();
	}

	cout << ans;
}