import numpy as np

grid_size = 5
grid_shape = (grid_size, grid_size)

def fill_grid_with_chain(grid_shape, shuffle_stripes=False, chain_linker=0):
    # define grid 
    m = np.zeros(grid_shape,dtype=np.int)
    # extract dimensions:
    grid_height, grid_width = grid_shape
    # "height" defines how many stripes would be there,
    # "width" determines the length of each stripe.
    # 
    # we'll pack a chain parallel to X:
    stripes = np.arange(grid_height,dtype=np.int)
    # shuffle those stripes if needed:
    if shuffle_stripes:
        np.random.shuffle(stripes)
    # fill in alternating stripes pattern ...
    start = 0 # chain index starts with 0:
    for count, stripe in enumerate(stripes):
        # stop of the linear/crystal/ordered segment:
        stop = start + grid_width
        # layout the chain alternatingly:
        if not count % 2:
            m[stripe,:] = np.arange(start,stop).astype(np.int)
        else:
            m[stripe,:] = np.arange(stop-1,start-1,step=-1).astype(np.int)
        # define "start" and "stop" along the folded chain segments:
        start = stop + chain_linker
    # return the state of the folded chain:
    return m




def dist_decay(mm, grid_size, linker):
    # dist_decay = {}
    chain_len_approx = grid_size*grid_size+linker*grid_size
    dist_decay = np.zeros(chain_len_approx, dtype=np.int)
    # ############################# # ...
    for i in range(grid_size):
        for j in range(grid_size):
            # let's analyze it:
            center = mm[i,j]
            if i>0:
                up = mm[i-1,j]
                dist_decay[abs(up-center)] += 1
            if i+1<grid_size:
                down = mm[i+1,j]
                dist_decay[abs(down-center)] += 1
            if j>0:
                left = mm[i,j-1]
                dist_decay[abs(left-center)] += 1
            if j+1<grid_size:
                right = mm[i,j+1]
                dist_decay[abs(right-center)] += 1
    #         dist_decay[]
    return dist_decay




