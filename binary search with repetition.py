def test_location(cards,query,mid):
    
    mid_number=cards[mid]
    
    
    
    #print(mid_number)
    
    if mid_number==query:
       
        if mid-1>0 and cards[mid-1]==query:
            
            return 'left'
        else:
            return 'found'
    elif mid_number<query:
        
        return 'left'
    else:
        
        return 'right'

def locate_card(cards,query):
    lo,hi,count = 0,len(cards)-1,0
    
    while lo<=hi:
        mid=(lo+hi)//2
        #count+=1
        
        results=test_location(cards,query,mid)
        count+=1
        if results=='found':
            
            print('no of cards opened: ',count)
            return mid
            
        elif results=='left':
            
            hi=mid-1
        elif results=='right':
           
            lo=mid+1
    return -1 
count=0
#test={{'cards':[9,7,6,4,3,2,1],'query': 6}
 #   'output': 2}
print(locate_card([8,8,6,6,6,6,6,3,2,2,2,0,0,0],8))

