def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        dis = 0
        for i in range(len(strand_a)):
            if strand_a[i] == strand_b[i]:
                pass
            else:
                dis += 1
        return dis
    else:
        raise ValueError('Not same length')



print (distance("ATCGGATV", "ATCGGATE"))