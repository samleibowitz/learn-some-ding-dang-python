names=['arya','samson','dora','tim','Ollivander']

max(len(name) for name in names)


max(names,key=lambda n:len(n))


songs=[
    {'title':'happy birthday','playcount':1},
    {'title':'survive','playcount':6},
    {'title':'YMCA','playcount':99},
    {'title':'Toxic','playcount':31},
]

min(songs,key= lambda song: song['playcount'])
max(songs,key= lambda song: song['playcount']))

