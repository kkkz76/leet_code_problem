def reverse_sum(list1,list2):
    list1.reverse() 
    list2.reverse()
    c=""
    d=""
    for x in list1:
        sc1= str(x)
        c+=sc1
    for z in list2:
        sc2= str(z)
        d+=sc2       
    total = int(c)+int(d)
    print(total)
    final_array = []
    for e in str(total):
        final_array.append(int(e))
    final_array.reverse()
    print(final_array)
  
list1 = [1,2,3]
list2 = [4,5,6]
print(list1)
print(list2)
reverse_sum(list1,list2)

