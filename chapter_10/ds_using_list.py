# This is my shopping list
shoplist = ["apple", "mango", "carrots", "banana"]

print "I have", len(shoplist), "items to purchase"

print "These items are:"

for item in shoplist:
    print item,

print "\nI also have to buy rice"
shoplist.append("rice")

print "My shopping list is now", shoplist

print "I will sort my list now"
shoplist.sort()

print "Sorted shopping list", shoplist

olditem = shoplist[0]
print "The first item I will buy is", olditem

del shoplist[0]
print "I bought the", olditem
print "My shoplist is now", shoplist
