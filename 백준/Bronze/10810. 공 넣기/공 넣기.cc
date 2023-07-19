#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    vector<int> v(n+1);
    
    for (int i = 0; i < m; i++)
    {
        int start, end, amount;
        cin >> start >> end >> amount;

        for (int j = start; j <= end; j++)
        {
            v[j] = amount;
        }
    }

    for (auto iter = v.begin() + 1; iter < v.end(); iter++)
    {
        cout << *iter << " ";
    }
    

}