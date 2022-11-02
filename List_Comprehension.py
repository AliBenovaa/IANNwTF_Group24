l1=[] #declare an empty list
l1=[x*x for x in list(range(1,100)) if (x%2==0)] #store the result of list comprehension in l1
print (l1)#print the list 