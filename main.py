import threading
import random
import time
import matplotlib.pyplot as plt

def sort1():
    global com1
    for iter1 in range(n1-1):
        for i in range(n1 - 1,iter1,-1):
            if arr[i - 1] > arr[i]:
                # print('sort1 = ', arr[i - 1], ', ', arr[i], ', i - 1 = ', i - 1, ', i = ', i)
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        com1 += 1
    com1 += 1
    # print('s1 died')
    return

def sort2():
    global com2
    for iter2 in range(n1,n1 + n2 - 1):
        for j in range(n1 + n2 - 1,iter2,-1):
            if arr[j - 1] > arr[j]:
                # print('sort2 = ', arr[j - 1],', ', arr[j], ', j - 1 = ', j - 1, ', j = ', j)
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
        com2 += 1
    com2 += 1
    # print('s2 died')
    return

def merge():
    global sortedArr, com1, com2
    left, right = 0, 0
    while left != n1 or right != n2:
        if (com1 != 0 or left == n1) and (com2 != 0 or right == n2):
            # print('merging')
            if right == n2:
                sortedArr[left + right] = arr[left]
                left += 1
                com1 -= 1
            elif left == n1:
                sortedArr[left + right] = arr[right + n1]
                right += 1
                com2 -= 1
            elif arr[left] < arr[right + n1]:
                sortedArr[left + right] = arr[left]
                left += 1
                com1 -= 1
            else:
                sortedArr[left + right] = arr[right + n1]
                right += 1
                com2 -= 1
    # print('m is dead', ', left = ', left, ', right = ', right)
    return


# join merge ---------------------------------------------------------------------
def sort12():
    for iter1 in range(n1-1):
        for i in range(n1 - 1,iter1,-1):
            if arr[i - 1] > arr[i]:
                # print('sort1 = ', arr[i - 1], ', ', arr[i], ', i - 1 = ', i - 1, ', i = ', i)
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    # print('s12 died')
    return

def sort22():
    for iter2 in range(n1,n1 + n2 - 1):
        for j in range(n1 + n2 - 1,iter2,-1):
            if arr[j - 1] > arr[j]:
                # print('sort2 = ', arr[j - 1],', ', arr[j], ', j - 1 = ', j - 1, ', j = ', j)
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    # print('s22 died')
    return

def merge2():
    global sortedArr
    left, right = 0, 0
    s12.join() and s22.join() # Waiting
    while left != n1 or right != n2:
        if right == n2:
            sortedArr[left + right] = arr[left]
            left += 1
        elif left == n1:
            sortedArr[left + right] = arr[right + n1]
            right += 1
        elif arr[left] < arr[right + n1]:
            sortedArr[left + right] = arr[left]
            left += 1
        else:
            sortedArr[left + right] = arr[right + n1]
            right += 1
    # print('m is dead', ', left = ', left, ', right = ', right)
    return

# Without Thread ------------------------------------------------------------
def merge3():
    global sortedArr
    left, right = 0, 0
    while left != n1 or right != n2:
        if right == n2:
            sortedArr[left + right] = arr[left]
            left += 1
        elif left == n1:
            sortedArr[left + right] = arr[right + n1]
            right += 1
        elif arr[left] < arr[right + n1]:
            sortedArr[left + right] = arr[left]
            left += 1
        else:
            sortedArr[left + right] = arr[right + n1]
            right += 1
    # print('m is dead', ', left = ', left, ', right = ', right)
    return

# heap sort ------------------------------------
def max_heapify(A,i,heapsize):
    l = 2*i + 1
    r = 2*(i + 1)
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        exchange(A,i,largest)
        max_heapify(A,largest,heapsize)

def Build_max_heap(A):
    for i in range(int((len(A) - 1) / 2), -1, -1):
        max_heapify(A, i, len(A))

def exchange(A,a,b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp

def Sort_Heap(A):
    Build_max_heap(A)
    heapsize = len(A)
    for i in range(len(A) - 1, 0, -1):
        exchange(A,0,i)
        heapsize = heapsize - 1
        max_heapify(A,0,heapsize)


# Randomized quicksort -----------------------------
def Sort_RandomizedQuicksort(A,p,r):
    if p < r:
        q = randomized_partition(A,p,r)
        Sort_RandomizedQuicksort(A,p,q - 1)
        Sort_RandomizedQuicksort(A, q + 1, r)

def randomized_partition(A,p,r):
    # i = randint(p,r)
    # exchange(A,r,i)
    return partition(A,p,r)

def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            exchange(A, i, j)
    exchange(A, i + 1, r)
    return i + 1


# Main -----------------------------------------------------------------------

NumberOfDataPoints = 50

Tthread1 = []
Tthread2 = []
Tthread3 = []
Tquick = []
Theap = []


arrSizes = random.sample(range(800,10001),NumberOfDataPoints)
arrSizes = sorted(arrSizes)

for arrSize in arrSizes:
    arr = random.sample(range(1,1000001), arrSize)
    sortedArr = [None] * arrSize
    arrCopy = arr[:]

    n2 = int(arrSize / 2)
    n1 = arrSize - n2
    com1 = 0
    com2 = 0

    # print('Array: ', arr)
    print('n1 = ', n1, ', n2 = ', n2)
    # Start 3 threads -------------------------------------
    tik = time.time()
    s1 = threading.Thread(name='sorting thread1', target = sort1)
    s2 = threading.Thread(name='sorting thread2', target=sort2)
    m = threading.Thread(name='merging thread', target=merge)

    s1.start()
    s2.start()
    m.start()


    m.join()
    # print('Sorted Array: ', sortedArr)
    tok = time.time()

    arr = arrCopy[:]
    sortedArr = [None] * arrSize
    # Start 2 threads ----------------------------------
    tik1 = time.time()
    s12 = threading.Thread(name='sorting thread1', target = sort1)
    s22 = threading.Thread(name='sorting thread2', target=sort2)
    m2 = threading.Thread(name='merging thread', target=merge2)

    s12.start()
    s22.start()
    m2.start()

    m2.join()

    tok1 = time.time()

    arr = arrCopy[:]
    sortedArr = [None] * arrSize
    # Start 1 thread -------------------------------------------------
    tik2 = time.time()
    sort12()
    sort22()
    merge3()
    tok2 = time.time()

    arr = arrCopy[:]
    sortedArr = arr

    # Start Heap Sort ------------------------------------------------
    tik3 = time.time()
    Sort_Heap(sortedArr)

    tok3 = time.time()

    arr = arrCopy[:]
    sortedArr = arr
    # Start Randomized Quick sort
    tik4 = time.time()
    Sort_RandomizedQuicksort(sortedArr, 0, len(sortedArr) - 1)

    tok4 = time.time()

    print('time 3 threads = ', (tok - tik)*1000, 'ms')
    print('time 2 threads = ', (tok1 - tik1)*1000, 'ms')
    print('time 1 threads = ', (tok2 - tik2)*1000, 'ms')
    print('time Heap Sort = ', (tok3 - tik3) * 1000, 'ms')
    print('time Randomized Quick sort = ', (tok4 - tik4) * 1000, 'ms')

    Tthread1.append((tok - tik)*1000)
    Tthread2.append((tok1 - tik1)*1000)
    Tthread3.append((tok2 - tik2)*1000)
    Theap.append((tok3 - tik3) * 1000)
    Tquick.append((tok4 - tik4) * 1000)


plt.plot(arrSizes, Tthread1, 'k--', label='Tthread1')
plt.plot(arrSizes, Tthread2, 'b:', label='Tthread2')
plt.plot(arrSizes, Tthread3, 'g-.', label='Tthread3')
plt.plot(arrSizes, Theap, 'm:', label='Heap')
plt.plot(arrSizes, Tquick, 'r', label='Quick')

plt.xlabel('Array Size')
plt.ylabel('Time(second)')

plt.title("Threads")

plt.legend()

plt.show()
