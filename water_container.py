def waterArea(height):
    total = []
    counter1=0
    for x in height:
        firstNum = x
        counter = 0
        counter1+=1
        for y in range(counter1,len(height)):
            
            counter+=1
            secNum = height[y]
            if firstNum < secNum:
                max1 = firstNum*counter
            if firstNum > secNum:
                max1 = secNum*counter
            else:
                max1 = firstNum*counter
            total.append(max1)
    print("Maximum Area:",max(total))
            
height = [1,8,6,2,5,4,8,3,7]
waterArea(height)