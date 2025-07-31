n = int(input('enter your number: '))
def pattern(n):
    lastline = n
    lastlinestars = n*4-1
    lastlineoneside = lastlinestars//2

    for i in range(1,n+1):
        if i==1:
            print(' '*lastlineoneside,' * ',' '*lastlineoneside)
        else:
            currentlinestars = i * 4 - 1
            currentlineoneside = currentlinestars // 2
            gapbetweenstars = lastlineoneside - currentlineoneside
            print(' '*gapbetweenstars,'*' * currentlineoneside,' ', '*' * currentlineoneside)

pattern(n)


n = int(input('enter your number: '))
def pattern(n):
    lastline = n
    lastlinestars = n*4-1
    lastlineoneside = lastlinestars // 2

    for i in range(1,n+1):
        if i==1:
            print(' '*lastlineoneside,' * ',' '*lastlineoneside)

        else:
            currentlinestars = i * 4 - 1
            currentlineoneside = currentlinestars // 2
            gapbetweenstars = lastlineoneside - currentlineoneside
            print(' '*gapbetweenstars,'*' * currentlineoneside,' ','*' * currentlineoneside)

pattern(n)


n = int(input('enter your number: '))
def pattern(n):
    lastline = n
    lastlinestars = n * 4 - 1
    lastlineoneside = lastlinestars // 2

    for i in range(1, n + 1):
        if i==1:
            print('*'+'$'*lastlineoneside)

        else:
            currentlinestars = i * 4 - 1
            currentlineoneside = currentlinestars // 2
            gapbetweenstars = lastlineoneside - currentlineoneside
            print(currentlineoneside*'*',gapbetweenstars*'$')

pattern(n)


n = int(input('enter your number: '))
def pattern(n):
    lastline = n
    lastlinestars = n * 4 - 1
    lastlineoneside = lastlinestars // 2

    for i in range(1, n + 1):
        if i==1:
            print(' ' * lastlineoneside, ' * ', ' ' * lastlineoneside)

        else:
            print('*',' ' * lastlineoneside, ' * ', ' ' * lastlineoneside,'*')


pattern(n)