#Using list comprehensions:

answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
#Using good old manual loops:

answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])
answer2 = []
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        answer2.append(num)


#Using list comprehensions(the more Pythonic way): 

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

cat='cat'




def is_palindrome(word):
    i=0
    i=len(word)
    string=None
    for i>=0:
        if word[i]!+' '
            string=string+word[i]
            i=i-1
        else:
            i=i-1
        return string