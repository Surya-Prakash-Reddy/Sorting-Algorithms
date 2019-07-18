#include<iostream>
#include<vector>
using namespace std;

void Merge(vector<int> &arr, int low, int mid, int high)
{
    vector<int> A, B;

    int n1 = mid-low+1;
    int n2 = high-mid;

    A.reserve(n1);
    B.reserve(n2);

    for(int i=0;i<n1;i++)
    {
        A.push_back(arr[low + i]);
    }
    for(int i=0;i<n2;i++)
    {
        B.push_back(arr[i + mid + 1]);
    }

    int i=0,j=0,k=low;

    while(i<n1 && j<n2)
    {
        if(A[i] <= B[j]) {
            arr[k] = A[i];
            i++;
        } else {
            arr[k] = B[j];
            j++;
        }
        k++;
    }
    while(i<n1)
    {
        arr[k] = A[i];
        k++;
        i++;
    }
    while(j<n2)
    {
        arr[k] = B[j];
        k++;
        j++;
    }
}

void MergeSort(vector<int> &arr, int low, int high)
{
    if(low<high) {
        int mid = (low+high)/2;
        MergeSort(arr, low, mid);
        MergeSort(arr, mid+1, high);

        Merge(arr, low, mid, high);
    }
}

int main()
{
    int n, temp;
    cout<<"Enter length of array: ";
    cin>>n;
    cout<<"\nEnter space separated "<<n<<" values: ";
    vector<int> arr;
    arr.reserve(n);
    for(int i=0;i<n;i++)
    {
        cin>>temp;
        arr.push_back(temp);
    }

    MergeSort(arr, 0, n-1);

    cout<<"\nAfter Sorting: ";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<"\n\n";
}
