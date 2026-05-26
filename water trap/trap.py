def trap(height):
    l = 0
    r = len(height)-1
    lmax=height[l]
    rmax=height[r]
    w=0
    while l<r:
        if lmax < rmax:
            l +=1
            lmax= max(lmax, height[l])
            w+=lmax-height[l]
        else:
            r -=1
            rmax= max(rmax, height[r])
            w+=rmax-height[r]
    return w
height=list(map(int,input("height:").split()))
print(trap(height))

