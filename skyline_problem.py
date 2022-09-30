
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
final_line = []

startPoint=0

def firstBuilding(a,b):
    
    leftMost_point=a[0]
    rightMost_point=a[1]
    height=a[2]
    startPoint
   
    if b==0 or buildings[b-1][1] < leftMost_point:
        line = [a[0],a[2]]
        final_line.append(line)

   
    else:

        if buildings[b-1][2] >  height:
            line = [buildings[b-1][1],a[2]]
            final_line.append(line)


        if b+1 == len(buildings):
            line = [a[1],0]
            final_line.append(line)
            return
            
        if buildings[b-1][2] <  height:
            line = [a[0],a[2]]
            final_line.append(line)

        if buildings[b+1][0] > rightMost_point:
            line = [a[1],0]
            final_line.append(line) 
 

for x in range(len(buildings)):
    firstBuilding(buildings[x],x)

print(final_line)
