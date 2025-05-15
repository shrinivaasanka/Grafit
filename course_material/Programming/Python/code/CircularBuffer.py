class CircularBuffer(object):
    def __init__(self,array):
        self.onedarray=array

    def circular_buffer_get(self,index):
        print("circula_buffer_get():","".join(self.onedarray))
        len1darray=len(self.onedarray)
        return self.onedarray[index%len1darray]

    def circular_buffer_set(self,index,value):
        len1darray=len(self.onedarray)
        self.onedarray[index%len1darray]=value
        print("circula_buffer_set():","".join(self.onedarray))
        return self.onedarray[index%len1darray]

    def circular_buffer_print(self, index):
        len1darray=len(self.onedarray)
        for n in range(index):
            print(self.onedarray[-n%len1darray:])
        print("iterations:",n)

if __name__=="__main__":
    x=['t','h','i','s',' ','i','s',' ','a',' ','s','e','n','t','e','n','c','e']
    cb=CircularBuffer(x)
    value=cb.circular_buffer_get(35)
    print("value get:",value)
    value=cb.circular_buffer_set(1000,value+' '+value)
    print("value set:",value)
    cb.circular_buffer_print(1000)
