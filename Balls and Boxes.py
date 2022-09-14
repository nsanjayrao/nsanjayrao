from itertools import combinations
for i in range(int(input())):
    no_of_balls,no_of_boxes=map(int,input().split())
    range_of_balls=[i for i in range(1,no_of_balls+1)]
    comb=combinations(range_of_balls,no_of_boxes)
    count=0   
    for i in comb:
        if sum(i)==no_of_balls:
            print(i,end=' ')
            count+=1
    print('\n','total_combinations: ',count)
    if count > 0:
        print('YES')
    else:
        print('NO')
