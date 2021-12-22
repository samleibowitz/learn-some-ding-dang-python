number=[1,2.3,4,5,6,7,7]

# index of will tell you the indext of something in a list 

number.index(5) # this will find 5 in you list and index it 

number.index(5.2) # this will look for 5 starting after the index of 2


number.index(5,2,6) # this will look for 5 after an index of 2 but bfore index of 6

# count returns the number of times x appears

number.count(2) # 1

number.count(21)# 0

number.count(7) #2


# reverse will reverse the order of a list

number.reverse #[7,7,6,5,4,3,2,1]

#sort will sort an itesam in place

another_list=[6,4,1,2,5]

another_list.sort() #[1,2,3,5,6]


# Join will join a list to a string

words=["Coding","Is","Fun"]

" ".join(words) # will join with a spcae between them 
                # if " " was "" it would concate them together

