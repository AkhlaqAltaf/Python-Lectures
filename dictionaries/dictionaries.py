# let start dictionary 

# dictionary is unordered collection of key-value pairs 
# each key associated with a value

# you can access a value with its coresponding key 
# dictionary extremely used for storing and retrieving data in a structured way 

# they are often refered as map and array in other languages 



# Creating Dictionary 

# there are two ways 


# 1

my_dict = {'name':"Akhlaq", 'age':25 , 'country':'pakistan'}

# 2
my_dict2 = dict(name ="Akhlaq" , country ='Pakistan' , city ="Jampur")


# Let Print 

# print(my_dict)
# print(my_dict2)





# access the value associated with key 
name = my_dict['name']

# print(name)


# adding new key and value 

my_dict['job'] = 'Software Developer And AI integration Specialist'


# print(my_dict)


# remove element from dictionary 


# del my_dict['age']

# print(my_dict)



# pop a value 

# pop mean it will get element and also delete it from dictionary 

# pop_element = my_dict.pop('name')
# print(pop_element)

# let check that element name deleted from dic or not 

# print(my_dict)



# check the existenece of element 

is_name = 'name' in my_dict
print(is_name)

# it should gave True 




# print all keys 

print(my_dict.keys())

# print all values 

print(my_dict.values())


# print length of dictionary 


print(len(my_dict))

