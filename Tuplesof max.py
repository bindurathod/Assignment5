list_of_tuples = [(9, 2, 7), (6, 8, 4), (3, 5, 1)]
 
list1 = [23,45]
list2 = [89,65,34]
list3 = [19,90,31,67]
 
def ret_2nd_ele(tuple_1):
    return tuple_1[1]

print("Min in list of tuples : ", min(list_of_tuples, key=ret_2nd_ele))

print("List with min length : ", min(list1,list2,list3,key=len))
