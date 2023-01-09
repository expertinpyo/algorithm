#include<iostream>
using namespace std;
int main(void) {

	int n = 0;
	int arr[30]={0,};
	
	for (int i = 0; i < 28; i++) {
		cin >> n;
		n -= 1;
		arr[n] = 1;
	}

	for (int i = 0; i < 30; i++) {
		if (arr[i] == 0) {
			cout << i + 1 << endl;;
		}
	}
}