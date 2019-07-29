'''
kasturi
justice sacchar
rashtriya shikha ayog
class 1&2
social workers and volunteers, stipend for them
retrired people

'''
import numpy as np
def Merge(A,B):
    n_compare,n_copy = 0,0
    C = [-1]*(len(A)+len(B))
    markerA,markerB = 0,0
    for markerC in range(len(C)):
        Aval,Bval = np.Inf,np.Inf
        n_compare += 1
        if markerA < len(A):
            Aval = A[markerA]
        n_compare += 1
        if markerB < len(B):
            Bval = B[markerB]
        n_compare += 1
        if Aval < Bval:
            markerA += 1
            val = Aval
        else:
            markerB += 1
            val = Bval
        C[markerC] = val
        n_copy += 1
    return C,n_compare,n_copy
    pass
def recMergeSort(ar,lower,upper):
    n_compare,n_copy = 0,0 
    if upper-lower+1 > 1:
        mid = (lower + upper)//2
        
        A,n_compare_,n_copy_ = recMergeSort(ar,lower,mid)
        n_compare += n_compare_
        n_copy += n_copy_
        
        B,n_compare_,n_copy_ = recMergeSort(ar,mid+1,upper)
        n_compare += n_compare_
        n_copy += n_copy_
    
        C,n_compare_,n_copy_ = Merge(A,B)
        n_compare += n_compare_
        n_copy += n_copy_
#        C = A+B
    else:
#        print(lower,upper)
#        print(ar[lower:upper+1])
        return ar[lower:upper+1],0,0
#    print(C)
    return C,n_compare,n_copy


if __name__ == '__main__':
    '''
    Test Merge
    '''
    if False:
        A = [1,2,5,18]
        B = [4,7,20,40]
        C,n_compare,n_copy = Merge(A,B)
        print(C)
    if True:
        A = [1,45,22,34,23,900,-1]
        sorted_A,n_compare,n_copy=recMergeSort(A,0,len(A)-1)
        print(sorted_A,n_compare,n_copy)
    
    pass
