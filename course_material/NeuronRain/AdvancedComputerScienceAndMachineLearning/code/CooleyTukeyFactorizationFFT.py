import cmath
import numpy as np
import subprocess
import json

def cooley_tukey_fft(N1,N2,x):
    FFTX=np.zeros(N2*N1+N2,dtype=complex)
    innerloop=0
    for k1 in range(0,N1-1):
        for k2 in range(0,N2-1):
            for n1 in range(0,N1-1):
                for n2 in range(0,N2-1):
                    innerloop+=x[N1*n2+n1]*cmath.exp(-2*cmath.pi*(0+1j)*n2*k2/N2)
                    #print("innerloop:",innerloop)
                outerloop=cmath.exp(-2*cmath.pi*(0+1j)*n1*(N2*k1+k2)/(N1*N2))
                #print("outerloop:",outerloop)
                FFTX[N2*k1+k2]=innerloop*outerloop
                innerloop=outerloop=0+0j
    print("FFTX:",FFTX)
    return FFTX

def factorization_and_fft(x=[1,2,3,4,5,6,7,8,9,10]):
    length=len(x)
    print("length:",length)
    subprocess.call(["/home/ksrinivasan/spark-3.3.0-bin-hadoop3/bin/spark-submit", "../../../../../asfer-github-code/python-src/DiscreteHyperbolicFactorizationUpperbound_TileSearch_Optimized.py", str(length), "1", "False","False","all","False"], shell=False)
    factorsfile = open("DiscreteHyperbolicFactorizationUpperbound_TileSearch_Optimized.factors")
    factors = json.load(factorsfile)
    print("factors:",factors)
    N1=int(factors[str(length)][0])
    print("N1:",N1)
    N2=int(length/N1)
    print("N2:",N2)
    cooley_tukey_fft(N1,N2,x)

if __name__=="__main__":
    x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    factorization_and_fft(x)

