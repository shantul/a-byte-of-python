zoo = ("lion", "tiger", "python")
print "Number of animals in the zoo is", len(zoo)
print "All animals in zoo are", zoo

new_zoo = ("monkey", "camel", zoo)
print "Number of cages in new zoo is", len(new_zoo)
print "All animals in new zoo are", new_zoo
print "All animals brought from old zoo are", new_zoo[2]
print "Last animal brought from old zoo was", new_zoo[2][2]
print "Number of animals in new zoo is", \
    len(new_zoo) - 1 + len(new_zoo[2])