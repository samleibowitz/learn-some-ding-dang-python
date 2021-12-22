#list comprehension sintax
#[__for__ in___] First line is what you want to do to the object or list, for is the variable you use in the list, in is the existing list 


name='john'
[char.upper() for char in name] # this creates a list of individual characthers in the sting ['J','O','H','N']

[num*10 for num in range(1,6)] #[10, 20, 30, 40, 50]


# converting a list of ints to stringas

numbers=[1,2,3,4,5,6]

[str(num) for num in numbers]