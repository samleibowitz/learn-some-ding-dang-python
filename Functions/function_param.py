def square(number):
    return number**2

def sing_happy_birthday(name):
    print('happy bday to you')
    print(f'happy birthday dear {name}')
    print('hppy bday to you')


element=[1,2,3]

 elif kwargs.get('operation')=='subtract':
        final_number=kwargs.get('first')-kwargs.get('second')
        if  kwargs.get('make_float')==True:
            final_number=float(final_number)
            return print(f'you subtracted {final_number}')
        else:
            final_number=int(final_number)
            return print(f'you subtracted {final_number}')
    elif kwargs.get('operation')=='multiply':
        final_number=kwargs.get('first')*kwargs.get('second')
        if  kwargs.get('make_float')==True:
            final_number=float(final_number)
            return print(f'you Multiplied {final_number}')
        else:
            final_number=int(final_number)
            return print(f'you Multiplied {final_number}')
     elif kwargs.get('operation')=='divide':
        final_number=kwargs.get('first')/kwargs.get('second')
        if  kwargs.get('make_float')==True:
            final_number=float(final_number)
            return print(f'you divided {final_number}')
        else:
            final_number=int(final_number)
            return print(f'you divided {final_number}')