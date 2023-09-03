#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class chess
{
public:
	int x;
	int y;
	int di;

	chess()
	{
		this->x = 0;
		this->y = 0;
		this->di = 0;
	};
	chess(int x, int y, int di)
		: x(x), y(y), di(di)
	{};

	void SetAxis(int x, int y)
	{
		this->x = x;
		this->y = y;
	}

	~chess()
	{};
};

int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };


int N, K;
vector<vector<int>> vMap(N, vector<int>(N));
vector<vector<vector<chess*>>> vArr(N);
vector<chess*> vChess;

void white(int nx, int ny, chess* ch)
{
	int x = ch->x;
	int y = ch->y;
	
	vector<chess*>& from = vArr[x][y];
	vector<chess*>& to = vArr[nx][ny];

	to.insert(to.end(), find(from.begin(), from.end(), ch), from.end());
	from.erase(find(from.begin(), from.end(), ch), from.end());
	
	for (auto iter_chess = to.begin(); iter_chess != to.end(); iter_chess++)
		(*iter_chess)->SetAxis(nx, ny);
	
}
void red(int nx, int ny, chess* ch)
{
	int x = ch->x;
	int y = ch->y;
	vector<chess*>& from = vArr[x][y];
	vector<chess*>& to = vArr[nx][ny];

	to.insert(to.end(), find(from.begin(), from.end(), ch), from.end());
	from.erase(find(from.begin(), from.end(), ch), from.end());

	reverse(find(to.begin(), to.end(), ch), to.end());
	
	for (auto iter_chess = to.begin(); iter_chess != to.end(); iter_chess++)
		(*iter_chess)->SetAxis(nx, ny);
}

void blue(chess* ch)
{
	if (ch->di % 2)
		ch->di--;
	else
		ch->di++;

	int nx = ch->x + dx[ch->di];
	int ny = ch->y + dy[ch->di];
	
	if (0 <= nx && nx < N && 0 <= ny && ny < N && vMap[nx][ny] != 2)
	{
		if (vMap[nx][ny] == 0)
			white(nx, ny, ch);
		else if(vMap[nx][ny] == 1)
			red(nx, ny, ch);
	}	
}

void deleteChess()
{
	for (auto ch : vChess)
		delete ch;
}

int main(int argc, char** argv)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> K;
	vMap.assign(N, vector<int>(N));
	vArr.assign(N, vector<vector<chess*>>(N));

	// 1. 배열 입력
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> vMap[i][j];	// 0 흰색 / 1 빨강 / 2 파랑
		}
	}
	// 2. 말 입력
	for (int i = 0; i < K; i++)
	{
		chess* ch = new chess();
		cin >> ch->x >> ch->y >> ch->di;
		ch->x--;
		ch->y--;
		ch->di--;
		vChess.push_back(ch);
		vArr[ch->x][ch->y].push_back(ch);
	}

	int ans = 1;
	while (ans <= 1000)
	{
		for (auto iter = vChess.begin(); iter != vChess.end(); iter++)
		{
			// 1. 갈 수 있는 곳 확인
			chess* ch = *iter;
			int nx = ch->x + dx[ch->di];
			int ny = ch->y + dy[ch->di];

			if (0 <= nx && nx < N && 0 <= ny && ny < N)
			{
				// 2. 이동하기
				switch (vMap[nx][ny])
				{
				case 0:
					white(nx, ny, ch);
					break;
				case 1:
					red(nx, ny, ch);
					break;
				case 2:
					blue(ch);
					break;
				}
			}
			else
				blue(ch);
			
			if (vArr[ch->x][ch->y].size() >= 4)
			{
				std::cout << ans << "\n";
				deleteChess();
				return 0;
			}
		}
		ans++;
	}
	std::cout << -1 << "\n";
	deleteChess();
}