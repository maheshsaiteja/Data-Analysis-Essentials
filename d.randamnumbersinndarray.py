#D.Random numbers in ndarray
#To create or get random numbers in numpy there is some special functions
import numpy as np
print("Random numbers in ndarray")
print("\n")
#getting some random float numbers with in 0 to 1 in 2*3 array
flt_ranarr=np.random.rand(2,3)
print("Random Rand")
print(flt_ranarr)
#Print some random float values from 5 to 10
flt_ran1=np.random.uniform(5,10,size=(2,3))
print("\nRandom Uniform")
print(flt_ran1)
#Print some random int values from 100 to 200
int_ran=np.random.randint(100,200,size=(4,3))
print("\nRandom Int")
print(int_ran)

