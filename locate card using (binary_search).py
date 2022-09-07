def locate_card(cards,query):
    lo,hi,count = 0,len(cards)-1,0
    while lo<=hi:
        mid=(lo+hi)//2
        mid_number=cards[mid]
        count+=1
        
        if mid_number==query:
            print('cards opened: {}'.format(count))
            return mid
            
        elif mid_number<query:
            hi=mid-1
        elif mid_number>query:
            lo=mid+1
    return -1
cards=[9,7,6,4,3,2,1]
query=6
print(locate_card(cards,query))
   
