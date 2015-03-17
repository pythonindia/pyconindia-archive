def load(path):
    res = []
    for line in file(path):
        res.append(int(line))
    return res

def flush(arr, path):
    with open(path, 'w') as fout:
        for item in arr:
            fout.write(str(item))
            fout.write('\n')

