first_list=[1,2,3,4]

first_list[1:] # starts at 2 and slices to the end [2,3,4]

first_list[3:] # starts at 4 and slices to the edn [4]


first_list[-1] # will start from the end of the list giving [4]



########list of colors##########

colors=["red","orange","yellow","green","blue","indigo","violet"]

colors[2:]

#slicing lists hold the same values, however not the same spot in memory

colors2=colors[:]

colors==colors2 #same values

colors is colors2 # different places in memeory


#### endPoint of slice #### 

# end points are EXLUCSIVZE


first_list[:2] # exlusive, will stop at 2, [1,2]

first_list[:4] #  will return all values since the index is only as high as 2

colors[:5]



### using the ::


first_list=[1,2,3,4,5,6]

first_list[1::2] # this is a step, starting at indext of 1 and skiping by 2 each time 


#swappiing values 

names=["James","Michelle"]

names[0],names[1]=names[1],names[0]

print(names)

