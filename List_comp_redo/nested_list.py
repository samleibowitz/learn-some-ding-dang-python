#nested list are list nested in lists

nested_list=[[1,2,3],[4,5,6],[7,8,9]]

nested_list[-1][1] #8


coords=[[10.423,9.132],[37.212,-14.092],[21.367,32.572]]


for loc in coords :
    for crd in loc:
        print(crd)

[[print(val) for val in ls] for ls in coords]


answer = [[num for num in range(0,10)] for l in range(0,10)]





person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {person[i]:person[i] for i in range(0,3)}



answer = {'aeiou':i for i in range(0,5)}