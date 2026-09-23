def array_slice_operations(array):
    print("array[:]:",array[:])
    for n in range(len(array)):
        print("array[-"+str(n)+":]:",array[-n:])
    for n in range(len(array)):
        print("array[:-"+str(n)+"]:",array[:-n])
    for n in range(len(array)):
        print("array[-"+str(n)+":"+str(n-len(array))+"]:",array[-n:n-len(array)])
    for n in range(len(array)):
        print("array["+str(n)+":]:",array[n:])
    for n in range(len(array)):
        print("array[:"+str(n)+"]:",array[:n])
    for n in range(len(array)):
        print("array["+str(n)+":"+str(len(array)-n)+"]:",array[n:len(array)-n])
    for n in range(len(array)):
        print("Ring buffer:",array[-n:]+array[:-n])

if __name__=="__main__":
    array_slice_operations([1,2,3,4,5,6,7,8,9,10])
    array_slice_operations("thisisastring")
