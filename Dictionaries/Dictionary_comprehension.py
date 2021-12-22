# dictonary comprehension {_____:___ for ___ in____}

numbers=dict(first=1,second=2,third=3)

square_num={key:values**2 for key,values in numbers.items()}




{num : num**2 for num in [1,2,3,4,5]}


instructor=dict(name='colt',city='San Fran',color='purple')

yelling_instructor={key:values.upper() for key,values in instructor.items()}

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
answer = {list1[i]: list2[i] for i in range(0,3)}
