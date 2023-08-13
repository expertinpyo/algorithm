#include<iostream>
#include<string>
#include<algorithm>

using namespace std;


string s;
string t;


bool check(string s, string t)
{
	if (s == t)
		return true;
	if (t.length() <= s.length())
		return false;
	if(t[t.length()-1] == 'A' && check(s, t.substr(0, t.length()-1)))
		return true;
	if (t[0] == 'B')
	{ 
		string rev = t.substr(1, t.length()-1);
		reverse(rev.begin(), rev.end());
		if(check(s, rev))
			return true;
	}
	return false;
}

int main(int argc, char** argv)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> s;
	cin >> t;

	bool ans = check(s, t);
	if (ans)
		cout << 1 << "\n";
	else
		cout << 0 << "\n";
}