ten_things="apple oranges crows telephone light sugar"
print"wait a minute, there are not ten things in the list,let's fix it"
stuff=ten_things.split(' ')
more_stuff=["days","night","song","fribee","corn","banana","girl","boys"]

while len(stuff)!=10:
    next_one=more_stuff.pop()
    print"Adding",next_one
    stuff.append(next_one)
    print"there are %d items now"%len(stuff)

print"there we go",stuff

print"let's do somethings with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print' '.join(stuff)
print'#'.join(stuff[3:5])