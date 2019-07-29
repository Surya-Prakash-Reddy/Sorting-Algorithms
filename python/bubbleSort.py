import numpy as np
from matplotlib import pyplot as plt
from utils import swap,test_performace
def bubbleSort(A):
    n_swap,n_compare = 0,0
    for i in range(len(A)-1):
        for j in range(i,len(A)-1):
            n_compare += 1
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                n_swap += 1
    benchmarks = {'n_compare':n_compare,'n_swap':n_swap}
    return A,benchmarks                
                
    return A
if __name__ == '__main__':
    if False:
        A = [23,1,78,-100,10]
        sorted_A,benchmarks= bubbleSort(A)
        print(sorted_A)
        print('len {} n_compare {} n_swap {}'.format(len(A),benchmarks['n_compare'],benchmarks['n_swap']))
    if True:
        test_performance(bubbleSort,lens = range(10),trials_per_len = 12)        

        
