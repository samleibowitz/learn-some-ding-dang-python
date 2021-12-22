def sum_args(*args):
    total=0
    for num in args:
        total=total+num
    return total 



def ensure_correct(*args):
    if "Colt" in args or 'steal' in args:
        return ' welcom back colt steal'
    else:
        return 'get out of here'