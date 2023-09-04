#include<iostream>
#include<vector>
#include<queue>
#include<limits>

using namespace std;

int maxValue = numeric_limits<int>::max();
int n, v, e;
int a, b;

vector<int> vHome;
vector<vector<pair<int, int>>> vRoad;

class comp
{
public:
	int weight;
	int node;

	comp(int weight, int node)
		:weight(weight), node(node)
	{};

	~comp()
	{};

	bool operator>(const comp& cp) const {
		return weight > cp.weight;
	}
};

int dijkstra(int x)
{
	vector<int> visited(v + 1);
	priority_queue<comp, vector<comp>, greater<comp>> heap;
	heap.push(comp(0, x));

	vector<int> dist(v + 1, maxValue);
	
	while (!heap.empty())
	{
		int weight = heap.top().weight;
		int node = heap.top().node;

		heap.pop();

		if (!visited[node])
		{
			visited[node] = 1;
			dist[node] = weight;

			for (auto iter = vRoad[node].begin(); iter != vRoad[node].end(); iter++)
			{
				if (!visited[iter->first] && dist[iter->first] > iter->second + weight)
				{
					heap.push(comp(iter->second + weight, iter->first));
				}
			}
		}
	}

	int result = 0;

	for (int nh : vHome)
	{
		if (dist[nh] < maxValue)
			result += dist[nh];
		else
			result--;
	}

	return result;
}

int main(int argc, char** argv)
{

	ios::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> n >> v >> e;
	cin >> a >> b;

	vRoad.assign(v + 1, vector <pair<int, int>>());

	for (int i = 1; i <= n; i++)
	{
		int input;
		cin >> input;
		vHome.push_back(input);
	}

	for (int i = 0; i < e; i++)
	{
		int start, end, value;

		cin >> start >> end >> value;
		vRoad[start].push_back({end, value });
		vRoad[end].push_back({ start, value });
	}

	int ans = 0;
	
	ans += dijkstra(a);
	ans += dijkstra(b);

	cout << ans << "\n";
		
}