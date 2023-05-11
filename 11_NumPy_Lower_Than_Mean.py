import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    totals = np.sum(weight * data[:, 1:], axis=1)
    mean = np.mean(totals)
    low = data[:,0][totals < mean]
    if len(low) == 0:
        print('None')
    else:
        print(', '.join(np.array(low, dtype=str)))

exec(input().strip())