items=["socks","mug","tea pot","cat food"]


items.clear() # this will deleate all ieams


items.pop() # will remove last nubmer by default

items.pop(1) # remove value at index of 1


items.remove('tea pot') # will remove first instace in list



#index 

number=[5,6,7,8,9,5]

number.index(6) #1

number.index(5,1) #5

# Create a list called instructors
instructors=[]

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt","Blue","Lisa"])
# Remove the last value in the list
instructors.pop()

# Remove the first value in the list
instructors.pop(0)

# Add the string "Done" to the beginning of the list
instructors.insert(0,"Done")


# Run the tests to make sure you've done this correctly!