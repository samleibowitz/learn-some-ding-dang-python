playlist=dict(
        Title='patigonia list', 
        author='colt',
        songs=[
            {'title':'song1','artist':['blue'],'duration':2.5},
            {'title':'song2','artist':['kitty','djcat'],'duration':5.5},
            {'title':'song3','artist':['kittycat','ddog'],'duration':5.5}

        ])
time=0
for songs in playlist['songs']:
    time=time+songs['duration']

print(time)