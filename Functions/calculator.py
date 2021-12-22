def calculate(**kwargs):
    final_number=1
    if kwargs.get('operation')=='add':
        final_number=kwargs.get('first')+kwargs.get('second')
        if  kwargs.get('make_float')==True:
            final_number=float(final_number)
            return print(f'you added {final_number}')
        else:
            final_number=int(final_number)
            return print(f'you added {final_number}')
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



