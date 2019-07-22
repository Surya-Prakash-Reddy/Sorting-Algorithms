#include<iostream>
#include<vector>
using namespace std;


int partition(vector<int> &v, int left, int right)
{
    int pivot = v[left];
    int i = left + 1;

    for(int j=left+1;j<=right;j++)
    {
        if(pivot >= v[j]) {
            swap(v[i], v[j]);
            i++;
        }
    }
    swap(v[i-1], v[left]);
    return i-1;
}

void QuickSort(vector<int> &v, int left, int right)
{
    if(left<right) {

        int partition_index = partition(v, left, right);

        QuickSort(v, left, partition_index-1);

        QuickSort(v, partition_index+1, right);
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
    QuickSort(v, 0, v.size()-1);

    cout<<"\nAfter Sorting: ";
    for(int i=0;i<n;i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<"\n\n";
}

