age=input('How Old Are you? ')

age=int(age)


if age>=21:
    print(f'coongrate at your age of {age} you can drink beer')
elif age<21 and age>=18:
    print(f'you are {age} you cant drink but you can party')
else :
    print(' sorry you need to be 21 to drink beer and 18 to party')