address_book = {"Shantul" : "shantul@github.com",
                "Larry": "larry@wall.org",
                "Spammer": "spammer@hotmail.co.uk",
                "Jack": "jack@pirate.com"
            }

print "There are {} contacts in the address book".format(len(address_book))
print "Shantul's address is", address_book["Shantul"]

#Deleting an entry from the dictionary
print "Deleting Spammer"
del address_book["Spammer"]
print "There are now {} contacts in the address book".format(len(address_book))

for name, address in address_book.items():
    print "Contact {} at {}".format(name, address)

print "Adding a new entry"
address_book["Guido"] = "guido@fawkes.com"

if "Guido" in address_book:
    print "Guido's address is", address_book["Guido"]
