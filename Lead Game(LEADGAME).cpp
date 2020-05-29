#include<iostream>
#include <cstdlib>
using namespace std;
int main(){
	int n=0;
	int Sum1=0,sum2=0;
	int leader=0,diff=0,lead=0,p1,p2;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>p1>>p2;
		Sum1+=p1;
		sum2+=p2;
		diff=abs(Sum1-sum2);
		if(diff>lead){
		    lead=diff;
		    leader=Sum1>sum2?1:2;
		}
		
	}
    cout<<leader<<" "<<lead;
	return 0;
}
