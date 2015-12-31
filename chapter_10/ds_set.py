bri = set(["brazil", "russia", "india"])

print bri

print "india" in bri

print "usa" in bri

bric = bri.copy()
bric.add("china")

print bric.issuperset(bri)

bric.remove("russia")

print bri & bric
print bri | bric
