nums=[1,2,3]


[x*10 for x in nums] # for all x in the list nums, multiple them by to


name='colt'

[char.upper() for char in name] # for all letters in the string name, capitilize them



[num*10 for num in range(1,10)]



#list comprehnsion

numbers=[1,2,3,4,5,6,7,8]

evens=[nums for num in numbers if num%2 ==0]

odds= [num for num in numbers if num%2!=0  ]





list=["elle","matt","John"]

answer=[x for x in list if  x in "emj"]