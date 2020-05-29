#include <iostream>
using namespace std;
int main() {
	// your code goes here
	int m,n;
	cin>>m;
	int books[m];
	for(int i=0;i<m;i++){
	    cin>>books[i];
	}
	cin>>n;
	int borrow[n];
	for(int i=0;i<n;i++){
	    cin>>borrow[i];
	    int index=borrow[i];
	   // cout<<"Index: "<<index<<endl;
	    cout<<books[index-1]<<endl;
	    for(int j=index-1;j<m-1;j++){
	        books[j]=books[j+1];
	    }
	}
	return 0;
}
