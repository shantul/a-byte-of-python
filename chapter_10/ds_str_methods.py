name = "Shantul"

if name.startswith("Sha"):
    print "Yes, name starts with 'Sha'"

if 'a' in name:
    print "Yes, there is an 'a' in", name

if name.find("han") != -1:
    print "Yes, 'han' is in", name

delimiter = "_*_"
mylist = ["Brazil", "Russia", "India", "China"]

print delimiter.join(mylist)
