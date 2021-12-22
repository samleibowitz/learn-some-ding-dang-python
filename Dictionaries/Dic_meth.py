#clear will cliar all values

d=dict(a=1,b=2,c=3)

d.clear()

#copy will copy a variable 

clone=d.copy()


#fromkeys will add a key to  this wil; become more usful later when we ask for user input

new_user={}.fromkeys(["name","score","email"],'uknown')

#get if a key is in a dictoray, it will pull a value, but it will return none over an error 

d.get("a")


d.get('f')



#pop takes a single argumen correpoding to a key and removes that key-value pair form the dictionary. Returns the calue corresponding to the key

d.pop('c') # {'a': 1, 'b': 2}

d.pop('iteam') # key calue error


#popitem will remove a iteam at random

d.popitem()


#update key value from one dictornairy to another. 

first=dict(a=1,b=2,c=3,d=4,e=5)

second={}

second.update(first) # this will take everything in the fist dict and add it to the second



inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD

stock_list={}

stock_list.update(inventory)

# add the value 18 to stock_list under the key "cookie"




# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop('cake')


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1:list2 for list1,list2 in list1}