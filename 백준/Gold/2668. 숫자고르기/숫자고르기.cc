#include<iostream>
#include<stack>
#include<set>
#include <unordered_set>

using namespace std;

int arr[101] = { 0 };
set<int> sAns;

int main(int argc, char** argv)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> arr[i];

	for (int i = 1; i <= n; i++)
	{
		if (sAns.find(i) != sAns.end())
			continue;

		if (arr[i] == i)
		{
			sAns.insert(i);
			continue;
		}
		
		stack<int> st;
		bool ok = false;
		unordered_set<int> visited;
		
		st.push(i);
		while (!st.empty())
		{
			int x = st.top();
			st.pop();

			visited.insert(x);

			if (arr[x] == i)
			{
				ok = true;
				break;
			}
			if (visited.find(arr[x]) == visited.end())
				st.push(arr[x]);
		}

		if(ok){
			for (auto iter = visited.begin(); iter != visited.end(); iter++)
			{
				if (sAns.find(*iter) == sAns.end())
					sAns.insert(*iter);
			}
		}
	}
	
	cout << sAns.size() << "\n";
	for (auto iter = sAns.begin(); iter != sAns.end(); iter++)
		cout << *iter << "\n";
}