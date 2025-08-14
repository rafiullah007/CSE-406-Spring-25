#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int n,head;
    cout<<"Enter number of Disk Request : ";
    cin>> n;

    int req[100];
    cout<<"Enter Disk Request Sequence : ";

    for(int i=0;i<n;i++)
    {
        cin>>req[i];
    }
    cout<<"Enter initial head position : ";
    cin>> head;

    int total_seak_op = 0;
    int current = head;

    cout<<"\nOrder of Execution : "<< current ;
    for(int i=0;i<n;i++)
    {
        if(req[i]!=current){
        total_seak_op += abs(req[i] - current);
        current = req[i];
        cout<< " -> "<<current ;
        }
    }
    cout<< "\n Total head movement : "<<total_seak_op<<endl;

    return 0;

}
