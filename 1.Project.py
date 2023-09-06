import random

def swg(c,m):
    if c==m:
        return None
    if (c=='water' and m=='gun'):
        return True
    elif (c=='gun' and m=='snake'):
        return True
    elif (c=='snake' and m=='water'):
        return True
    else:
        return False
    

choice=('snake','water','gun')
computer=random.randint(0,2)
computer=choice[computer]
man=input('choose either water or gun or snake: ' )
win=swg(computer,man)
print(f'You choose {man} and computer choose {computer}:')
if win is None:
    print('Match draw')
elif win:
    print('You loose the match')
else:
    print('You won the match')

