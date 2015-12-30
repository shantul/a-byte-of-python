number = 23
guess = int(raw_input('Enter an integer: '))

if guess == number:
    print 'Congratulations, you guess it. \n(but you do not win any prizes!)'
elif guess < number:
    print 'No, it is a little higher than than'
else:
    print 'No, it is a little lower than that'

print 'Done'
