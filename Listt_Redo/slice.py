# slice will slice down portions of a list


# some_list[start:end:step]


# first parameter for slice:start 

first_list=[1,2,3,4]

first_list[1:] # [2,3,4]

first_list[3:] # [4] 

first_list[-2] # [3,4]

#second parameter :ends, exculsive 


first_list=[1,2,3,4]

first_list[:2] #[1,2]

first_list[:4] #[1,2,3,4]

first_list[1:3] #[2,3]

# third parameter is the step, counnts on an interation

first_list=[1,2,3,4,5,6,7,8]

first_list[1::2] #[2,4,6,8]

first_list[::2] #[1,3,5,7]

# with negative numbers it reveeses the list, does not start from the end of the list

first_list[1::-1] # START AT 2 AND GOES BACKWARDS [2,1] 

first_list[:1:-1] # WE ARE ENDING AT 1 BUT STARTING FORM THE BACK OF THE ARRAY


#modifyinfg a list with a slice 

numbers=[1,2,3,4,5]
numbers[1:3]=['a','b','c']


###sqaping values@@


#swappiing values 

names=["James","Michelle"]

names[0],names[1]=names[1],names[0]

print(names)






