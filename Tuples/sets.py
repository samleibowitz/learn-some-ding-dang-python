set2={1,2,3,4}

for set in set:
    print(set)


set2.add(7)

set2.remove(2) # will prouce an error if not there 

set.discard(2) # will discard without an error



###set math



set2={1,2,3,4,5,6}

set3={4,5,6,7,8,9}


set2 | set3 # this will return the unioun of two sets


set2 & set3 # this will return the intersection