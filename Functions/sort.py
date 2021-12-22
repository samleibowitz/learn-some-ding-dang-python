nums=[2,3,4,5,6]

nums.sort() #[2,34,5,6]

sorted(nums,reverse=True) #6,5,4,3,2,1


user=[
    {'usernae':'samuel','tweet':['I love cats','I love dogs']},
    {'usernae':'katie','tweet':['I love cats']},
    {'usernae':'jeff','tweet':[]},
    {'usernae':'bob123','tweet':['I love dogs']},
    {'usernae':'gat_gurl','tweet':[]}]

sorted(user,key=lambda user: user['usernae'])
sorted(user,key=lambda user: len(user['tweet']))



songs=[
    {'title':'happy birthday','playcount':1},
    {'title':'survive','playcount':6},
    {'title':'YMCA','playcount':99},
    {'title':'Toxic','playcount':31},
]

sorted(songs,key=lambda songs: songs['playcount'],reverse=True)