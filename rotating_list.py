def no_of_rotating_list(arr,sor_arr):
    res=True
    rotation=0
    while res:
        item=arr.pop()
        arr.insert(0,item)
        if arr==sor_arr:
            res=False
            break
        rotation+=1
    return rotation
    
    
    
arr=list(map(int,input().split()))
sor_arr=list(map(int,input().split()))
print(no_of_rotating_list(arr,sor_arr))
