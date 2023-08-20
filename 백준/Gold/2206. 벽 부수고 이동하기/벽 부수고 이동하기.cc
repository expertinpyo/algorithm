#include<iostream>
#include<vector>
#include<deque>
#include <limits>

using namespace std;
class axis
{
public:
	int x;
	int y;
	bool wall;
	int cnt;

	axis(int x, int y, bool wall, int cnt)
		: x(x), y(y), wall(wall), cnt(cnt)
	{
	};

	~axis()
	{
	};
};

int n, m;
vector<vector<int>> vArr;

int maxValue = numeric_limits<int>::max();


int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int bfs()
{
	deque<axis> que;
	que.push_back(axis(0, 0, true, 1));

	vector<vector<bool>> visited_zero(n, vector<bool>(m, 0));
	vector<vector<bool>> visited_one(n, vector<bool>(m, 0));

	int ans = maxValue;
	visited_zero[0][0] = true;

	while (!que.empty())
	{
		int x = que.front().x;
		int y = que.front().y;
		bool wall = que.front().wall;
		int cnt = que.front().cnt;

		que.pop_front();

		for (int d = 0; d < 4; d++)
		{
			int nx = x + dx[d];
			int ny = y + dy[d];

			if (0 <= nx && nx < n && 0 <= ny && ny < m)
			{
				if (nx == n-1 && ny == m-1)
				{
					ans = min(ans, cnt + 1);
					continue;
				}

				if (!vArr[nx][ny])
				{
					if (wall && !visited_zero[nx][ny])
					{
						que.push_back(axis(nx, ny, wall, cnt + 1));
						visited_zero[nx][ny] = true;
					}
					else if (!wall && !visited_one[nx][ny])
					{
						que.push_back(axis(nx, ny, wall, cnt + 1));
						visited_one[nx][ny] = true;
					}
				}
				else
				{
					if (wall && !visited_one[nx][ny])
					{
						que.push_back(axis(nx, ny, false, cnt + 1));
						visited_one[nx][ny] = true;
					}
				}
				
			}
		}
	}

	if (ans == maxValue)
		ans = -1;
	return ans;

}

int main(int argc, char** argv)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m;

	vArr.assign(n, vector<int>(m, 0));

	for (int i = 0; i < n; i++)
	{
		string str;
		cin >> str;

		for (int j = 0; j < m; j++)
		{
			if (str[j] != '0')
				vArr[i][j] = 1;
		}
	}
	if (n == 1 && m == 1)
		cout << 1 << "\n";
	else
		cout << bfs() << "\n";

}