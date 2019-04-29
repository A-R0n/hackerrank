## Perform d rotations on list a:
def rotLeft(a, d):
    return a[d:] + a[:d]
## Every element to the right of d will be shifted left
## and every element before d will be added to the end.