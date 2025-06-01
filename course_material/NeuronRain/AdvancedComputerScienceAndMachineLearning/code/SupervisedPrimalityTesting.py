def test_primality(p,k,S):
    for s in S:
         if p%s==0:
            print(str(p)+" is composite")
            return
    print(str(p)+" is prime")

if __name__=="__main__":
    p=391
    #k must be closest integer greater than square root of p - at present set manually
    k=20
    #Set S contains all prime numbers less than k - at present set manually
    S=[2,3,5,7,11,13,17,19]
    for n in range(p-60,p+60):
        test_primality(n,k,S)
