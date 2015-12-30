def total (initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        print "printing number", number
        count += number

    for key in keywords:
        print "printing keywords", keywords
        count += keywords[key]

    print count

total(5, 1, 2, 3, 10, 20,vegetables=10, fruits=50)

