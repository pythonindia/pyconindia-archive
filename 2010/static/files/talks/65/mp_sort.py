import sys
import time
import multiprocessing

from merge_sort import *
from sort_helpers import *

def split(arr, n):
    part_len = len(arr) / n
    if part_len == 0:
        return arr
    res = []
    for i in range(0, n - 1):
        beg = i * part_len
        end = beg + part_len
        res.append(arr[beg : end])
    res.append(arr[(n - 1) * part_len : ])
    return res

def merge_all(arrays):
    res = []
    for i in range(0, len(arrays)):
        res = merge(res, arrays[i])
    return res
    
if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "usage: merge_sort.py <in> <out>"
		sys.exit(-1)

	workers = multiprocessing.cpu_count()
	pool = multiprocessing.Pool(workers)

	arr = load(sys.argv[1])
		
	start = time.time()
	splices = split(arr, workers)
	res = pool.map(merge_sort, splices)
	res = merge_all(res)
	stop = time.time()
	  
	flush(res, sys.argv[2])
	print "Time taken: %f seconds" % ((stop - start))
   
