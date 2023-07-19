#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;


int main()
{
    double result = 0;
    int cnt = 0;
    map<string, float> table;
    table.insert({ "A+", 4.5 });
    table.insert({ "A0", 4.0 });
    table.insert({ "B+", 3.5 });
    table.insert({ "B0", 3.0 });
    table.insert({ "C+", 2.5 });
    table.insert({ "C0", 2.0 });
    table.insert({ "D+", 1.5 });
    table.insert({ "D0", 1.0 });
    table.insert({ "F", 0 });

    for (int i = 0; i < 20; i++)
    {
        string name, grade;
        double point;

        cin >> name >> point >> grade;

        if (grade.compare("P"))
        {
            cnt += point;
            result += table[grade]*point;
        }
    }

    cout << result / cnt;

}