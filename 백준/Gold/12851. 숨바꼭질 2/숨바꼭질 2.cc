#include <iostream>
#include <queue>
#include <map>

using namespace std;

map<int, int> mAnswer; // 최종 정답이 담기는 map

void bfs(int n, int k)
{
	queue<int>que;	// n->k를 찾기 위한 queue

	int dist[100001] = { 0, };		  // count
	que.push(n);
	

	while (!que.empty())
	{
		int x = que.front();
		que.pop();

		int arr[3] = { x - 1, x + 1, x * 2 };

		for (int idx = 0; idx < 3; idx++)
		{
			int nx = arr[idx];

			if (0 <= nx && nx <= 100000 && (!dist[nx] || dist[x] + 1 <= dist[nx]))
			{
				if (nx == k)
				{
					dist[nx] = dist[x] + 1;

					if (mAnswer.find(dist[nx]) == mAnswer.end())
						mAnswer[dist[nx]] = 0;
					mAnswer[dist[nx]] += 1;
				}
				que.push(nx);
				dist[nx] = dist[x] + 1;
			}
		}
	}
}

int main()
{
	int n, k;
	cin >> n >> k;

	if (n == k)
	{
		cout << 0 << "\n";
		cout << 1;
		return 0;
	}
	bfs(n, k);
	
	auto iter = mAnswer.begin();
	if(iter != mAnswer.end())
	{ 
		cout << iter->first << "\n";
		cout << iter->second;
	}
	
}