# Now we discuss tuple data structure 

# Tuples are immutable and list are mutable data structure 
# it mean when you create a tuple you cannot change its contents 

# you cannot add or remove or modify 
# it is usefull when you want to create constant data structure 


# le start operations of tuple 


# we can create a tuple in two ways 


# with parenthesis

tuple1=('Akhlaq','Ali','Taveer','Mudasir' , 'Akhlaq')
tuple2 = 'Akhlaq','Ali','Tanveer','Mudasir'

# these both are same 

# let check 


# for items in tuple1:

#     print(items)



# for items in tuple2:

#     print(items)




# sub-tuple in tuple 


# sub_tuple = tuple1[1:3]

# print(sub_tuple)


# repeated tuple 

# rep_tuple = tuple1 *2

# it will print same data two time 


# print(rep_tuple)



# access element in new variables
# 
#  

# we have four elements so we create 4 new variables 
a,b,c , d ,e= tuple1

# print(a)
# print(b)
# print(c)
# print(d)



# count that an element exist how many time in tuple


count_akhlaq = tuple1.count('Akhlaq')

# print(count_akhlaq)






# let add two time and check 



# access element with index 

index_element = tuple1[2]

# print(index_element)


# check index of element 


index = tuple1.index('Taveer')

print(index)

