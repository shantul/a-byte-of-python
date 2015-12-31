number = 10
running = True

while running:
    guess = int(raw_input('Hi Miraya. Enter an number: '))

    if guess == number:
        print 'Congratulations, you guess it. \n(but you do not win any prizes!)'
        running = False
    elif guess < number:
        print 'No, it is a little higher than that'
    else:
        print 'No, it is a little lower than that'
else:
    print 'The while loop is over'

print 'Done'
