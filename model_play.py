import numpy as np


grid_size = 5

m = np.zeros((grid_size,grid_size))

# x[0,:] = np.arange(0,5)
# x[4,:] = np.arange(10,5,-1)

counts = np.arange(grid_size,dtype=np.int)
stripes = np.arange(grid_size,dtype=np.int)
# shuffle those stripes ...
np.random.shuffle(stripes)
# fill in alternating stripes pattern ...
for count, stripe in zip(counts,stripes):
    if count % 2:
        start = count*grid_size
        stop  = (count+1)*grid_size
        m[stripe,:] = np.arange(start,stop)
    else:
        start = count*grid_size
        stop  = (count+1)*grid_size
        m[stripe,:] = np.arange(stop-1,start-1,step=-1)










