import numpy as np

def similarity(tqz1,tqz2, max_stdv = 0.7):
    difference_array = []
    for index in range(len(tqz1)):
        difference_array.append(tqz1[index] - tqz2[index])
    standard_deviation = np.std(difference_array)
    return (1 - standard_deviation/max_stdv) * 100    
