#include<iostream>
using namespace std;
int main()
{
	int n,x,r=0,sum=0,v1[200001];
	cin>>n;
	for(int i=0;i<n;i++)
	{
	    cin>>v1[i];
	}
	for(int i=0;i<n;i++)
	{
		for(int j=i;j<n;j++)
		{
			if(i!=j){
				if(v1[i]<v1[j]){
					r=v1[j]-v1[i];
				}
				else{
				
			r=v1[i]-v1[j];
		}
			sum=sum+r;	
		}}
	}
	cout<<sum;
	return 0;
}
