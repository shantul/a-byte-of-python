print "Simple Assignment"
shoplist = ["apple", "mango", "banana", "carrots"]
#mylist is just another name pointing to the same object

mylist = shoplist

#removing first item from shoplist
del shoplist[0]

print "shoplist is", shoplist
print "mylist is", mylist

print "Copy by making a full slice"
mylist = shoplist[:]

#removing first item from shoplist
del shoplist[0]

print "shoplist is", shoplist
print "mylist is", mylist
