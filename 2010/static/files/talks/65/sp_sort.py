import sys
import time

from merge_sort import *
from sort_helpers import *

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: %s <in> <out>" % (sys.argv[0])
        sys.exit(-1)

    arr = load(sys.argv[1])
    
    start = time.time()
    arr = merge_sort(arr)
    stop = time.time()
  
    flush(arr, sys.argv[2])
    print "Time taken: %f seconds" % ((stop - start))
