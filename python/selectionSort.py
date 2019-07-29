from utils import swap,test_performance
def selectionSort(A):
    n_compare,n_swap =0,0
    
    for i in range(len(A)):
        least_ix = len(A)-1
        for j in range(i,len(A)):
            n_compare +=1
            if A[j]<A[least_ix]:
                least_ix = j
        swap(A,i,least_ix)
        n_swap +=1
    benchmarks = {'n_compare':n_compare,'n_swap':n_swap}
    return A,benchmarks
    
if __name__ == '__main__':
    if False:
        A = [23,1,78,-100,10]
        sorted_A,benchmarks=selectionSort(A)
        print(sorted_A,benchmarks['n_compare'],benchmarks['n_swap'])
    if True:
        test_performance(selectionSort)
