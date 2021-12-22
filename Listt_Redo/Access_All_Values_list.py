
numbers=[1,2,3,4]

for k in numbers:  # this will print all number in list
    print(k)


### we can also print with mathematical operations on a loop

for k in numbers:
    print(k*k) # this will square the nmbers


#we can also use a while loop to run throuhg a list of numbers


i=0
while i<len(numbers):
    print(numbers[i])
    i+=1

# this strength of while loop is the fact that we can acccess the index
k=0
while k<len(numbers):
    print(f'this is the numbe r{numbers[k]} at index {k}')
    k+=1

matt= "MATT"

matt.lower()