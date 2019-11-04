from SortedPriorityList import SortedPriorityQueue

def queueInsertionSort(array):
    p = SortedPriorityQueue()
    r = []
    for n in array:
        p.add(n, n)
    for i in range(0, len(p)):
        r.append(p.remove_min()[0])
    return r




if __name__ == '__main__':
    s1 = [1, 2, 5, 6, 7, 8, 5, 4, 7, 12, 45, 234, 56, 23]
    s2 = queueInsertionSort(s1)
    for i in s2:
        print(i)