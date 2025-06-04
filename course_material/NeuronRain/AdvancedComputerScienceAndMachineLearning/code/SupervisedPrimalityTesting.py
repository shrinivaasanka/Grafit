import math
import sys

def test_primality(p,k,S):
    for s in S:
         if p%s==0:
            print(str(p)+" is composite")
            return False
    print(str(p)+" is prime")
    return True

if __name__=="__main__":
    maxp=int(sys.argv[1])
    p=2
    #k must be closest integer greater than square root of p - Newton-Raphson square root algorithm is invoked 
    k=int(math.sqrt(p) + 1)
    #Set S contains all prime numbers less than or equal to k
    S=[2]
    while p < maxp:
        isprime=test_primality(p,k,S)
        if isprime:
            S.append(p)
            print("List of primes S updated to:",S)
        print("Verification of Prime Number Theorem estimate :",p/math.log(p)," and actual size of S:",len(S))
        p+=1
        k=int(math.sqrt(p) + 1)

