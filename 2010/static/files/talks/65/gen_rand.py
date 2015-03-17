import sys
import random

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: %s <min> <max>" % (sys.argv[0])
        sys.exit(-1)


    random.seed()

    rmin = int(sys.argv[1])
    rmax = int(sys.argv[2])
    count = rmax - rmin

    for i in range(0, count):
        print random.randint(rmin, rmax)
