#include<iostream>
#include<vector>
using namespace std;

void BubbleSort(vector<int> &v)
{
    for(int i=0;i<v.size()-1;i++)
    {
        for(int j=0;j<v.size()-i-1;j++)
        {
            if(v[j] > v[j+1]) {
                swap(v[j], v[j+1]);
            }
        }
    }
}

int main()
{
    vector<int> v;
    int n, temp;
    cout<<"Enter the number of values to sort: ";
    cin>>n;

    cout<<"\nEnter space separated "<<n<<" values: ";
    for(int i=0;i<n;i++)
    {
        cin>>temp;
        v.push_back(temp);
    }
    BubbleSort(v);

    cout<<"\nAfter Sorting: ";
    for(int i=0;i<n;i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<"\n\n";
}


