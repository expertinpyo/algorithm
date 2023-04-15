#include <iostream>
#include <queue>
#include <tuple>
#include <map>

using namespace std;


bool arr[100][100] = { 0, };
int maps[100][100] = { 0, };

int n;
int continent = 1;

int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

int main()
{
	cin >> n;
	
	// 항상 두개 이상의 섬 존재

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> arr[i][j];
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (arr[i][j] && !maps[i][j])
			{
				queue<pair<int, int>> queue;
				maps[i][j] = continent;
				queue.push(make_pair(i, j));
				while (queue.size())
				{
					int x = queue.front().first;
					int y = queue.front().second;
					queue.pop();
					for (int k = 0; k < 4; k++)
					{
						int nx, ny;
						nx = x + dx[k];
						ny = y + dy[k];
						if (0 <= nx && nx < n && 0 <= ny && ny < n && arr[nx][ny] && !maps[nx][ny])
						{
							maps[nx][ny] = continent;
							queue.push({ nx, ny });
						}
							
					}
				}
				continent += 1;
			}
		}
	}
	int ans = 100000;

	map<int, int> m;
	
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (maps[i][j] && m.find(maps[i][j]) == m.end())
			{
				m.insert({ maps[i][j], 0 });
				bool visited[100][100] = { false, };
				queue<tuple<int, int, int>> queue;
				queue.push(make_tuple(i, j, 0));
				visited[i][j] = true;

				while (queue.size())
				{
					int x, y, cnt;
					tie(x, y, cnt) = queue.front();

					queue.pop();

					for (int k = 0; k < 4; k++)
					{
						int nx, ny;
						nx = x + dx[k];
						ny = y + dy[k];
						if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && cnt < ans) 
						{
							visited[nx][ny] = true;
							if (maps[nx][ny] == maps[i][j])
								queue.push(make_tuple(nx, ny, cnt));
							else
								if (!maps[nx][ny])
									queue.push(make_tuple(nx, ny, cnt + 1));
								else
									ans = cnt;
						}
					} 
				}
			}
		}
	}
	cout << ans << endl;
}