import numpy as np 

arr=np.array([
    [1,2,3],
    [7,5,6],
    [7,8,9]
])
print(arr)
print(np.mean(arr,axis=0))
print(np.median(arr,axis=0))# if axis = 1 it will calculate rows and axis =0 then it will calculte coulmn