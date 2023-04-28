def while_loop():
    x=1
    while x<10:
        print(x)
        x+=1

def break_statement():
    x=1
    while x<10:
        print(x)
        if x==5:
            break
        x+=1

def continue_statement():
    x=1
    while x<10:
        x+=1
        if x%2!=0:
            continue
        print(x)
