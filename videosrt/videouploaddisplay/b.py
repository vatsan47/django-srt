import re

mylist = ["dog", "cat is good", "wildcat", "thundercat", "cow", "hooo"]
# newlist = list(filter(r.match, mylist))
# print(newlist)
for i in mylist:
    print(re.match("cat", i))