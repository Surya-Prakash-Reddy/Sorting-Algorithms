from utils import test_performance
def insertionSort(A):
    n_compare,n_copy = 0,0    
    if len(A) == 0:
        benchmarks = {'n_compare':n_compare,'n_copy':n_copy} 
        return A,benchmarks
    for i in range(1,len(A)):
        j=0 
        while j<i:
            n_compare += 1
            if A[j]>A[i]:
                temp = A[i]
                A[j+1:i+1] = A[j:i]
                A[j] = temp
                n_copy = 1 + 1 + i-j + 1
                break
            j+=1
    benchmarks = {'n_compare':n_compare,'n_copy':n_copy} 
    return A,benchmarks
if __name__ == '__main__':
    if False:
        A = [23,1,78,-100,10]
        sorted_A,benchmarks = insertionSort(A)
        print(sorted_A,benchmarks['n_compare'],benchmarks['n_copy'])
    if True:
        test_performance(insertionSort,lens = range(10),trials_per_len = 12)  
