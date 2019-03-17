guessme = 10
start = 11
while True:
    if start < guessme:
        print("Too Low")
    elif start == guessme:
        print('Found it!')
        break
    elif start > guessme:
        print('OOPS')
        break
    start += 1
