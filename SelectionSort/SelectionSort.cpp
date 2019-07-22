#include<iostream>
#include<vector>
using namespace std;

void SelectionSort(vector<int> &v)
{
    int temp, index;
    for(int i=0;i<v.size()-1;i++)
    {
        index = i;
        for(int j=i+1;j<v.size();j++)
        {
            if(v[index] > v[j]) {
                index = j;
            }
        }

        temp = v[i];
        v[i] = v[index];
        v[index] = temp;
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
    SelectionSort(v);

    cout<<"\nAfter Sorting: ";
    for(int i=0;i<n;i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<"\n\n";
}

