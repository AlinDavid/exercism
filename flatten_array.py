def flatten(iterable):
    
    output = []
    
    for i in iterable:
        if (isinstance(i,list)):
            output = output + flatten(i)
        else:
            output = output + [i] if (i != None) else output
            
    return output
