#include<iostream>
#include<vector>
using namespace std;

void InsertionSort(vector<int> &v)
{
    int j, value;
    for(int i=1;i<v.size();i++)
    {
        value = v[i];

        for(j=i-1;j>=0;j--)
        {
            if(v[j] > value) {
                v[j+1] = v[j];
            } else {
                break;
            }
        }
        v[j+1] = value;
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
    InsertionSort(v);

    cout<<"\nAfter Sorting: ";
    for(int i=0;i<n;i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<"\n\n";
}

