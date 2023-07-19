#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    vector<int> v(n+1);
    
    for (int i = 0; i <= n; i++)
    {
        v[i] = i;
    }

    for (int i = 0; i < m; i++)
    {
        int left, right;
        cin >> left >> right;

        int left_value = v[left];
        int right_value = v[right];

        v[left] = right_value;
        v[right] = left_value;

    }

    for (auto iter = v.begin() + 1; iter < v.end(); iter++)
    {
        cout << *iter << " ";
    }
    

}