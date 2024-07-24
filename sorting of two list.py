def sort_list(list1,list2):
    sorted_list=sorted(set(list1+list2))
    if len(list1)==len(list2):
        print("Size of two list are equal,\nascending order")
        sorted_list.sort()
    else:
        print("size of two list are not equal.\ndescending order")
        sorted_list.sort(reverse=True)
    return sorted_list
while True:
    try:
        n1=int(input("enter the size of list 1:"))
        n2=int(input("enter the size of list 2:"))
        if n1<=0 or n2<=0:
            print("please enter the positive size of list!!!!")
        else:
            break
    except ValueError:
        print("invalid input.please enter the integer for list!!!!")
list1=[]
for i in range(n1):
    while True:
        try:
            l1=int(input("enter the elements for list 1:"))
            list1.append(l1)
            break
        except ValueError:
            print("Invalid input .Please enter the integer value!!!")
list2=[]
for i in range(n2):
    while True:
        try:
            l2=int(input("enter the elements for list2:"))
            list2.append(l2)
            break
        except ValueError:
            print("Invalud input.Please enter the integer value!!!")
result=sort_list(list1,list2)
print("sorted list:",result)



