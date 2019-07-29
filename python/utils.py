import numpy as np
from matplotlib import pyplot as plt
def swap(a,ix1,ix2):
    temp = a[ix1]
    a[ix1] = a[ix2]
    a[ix2] = temp

def test_performance(algo,lens = range(10),trials_per_len = 12):

    compare_means = []
    compare_std = []

    swap_means = []
    swap_std = []
    
    means = {}
    stds = {}
    for l in lens:
#        l_compare = []
#        l_swap = []
        benchmarks_l = {}
        for t in range(trials_per_len):
            A = np.random.random(l)
            sorted_A,benchmarks_t= algo(A)
            
            for k in benchmarks_t:
                if k not in benchmarks_l:
                     benchmarks_l[k] = []
                benchmarks_l[k].append(benchmarks_t[k])
            
#            l_compare.append(benchmarks['n_compare'])
#            l_swap.append(benchmarks['n_swap'])

        for k in benchmarks_l:
            if k not in means:
                 means[k] = []
            if k not in stds:
                 stds[k] = []
            
            means[k].append(np.mean(benchmarks_l[k]))
            stds[k].append(np.std(benchmarks_l[k]))

    
    for k in means:
        plt.figure()
        plt.plot(lens,means[k])
        plt.title('{} vs array length'.format(k))
        plt.show()
    
#    plt.figure()
#    plt.plot(lens,swap_means)
#    plt.title('swaps vs array length')
#    plt.show()
        
