import hashmap
#create a mapping of state to abbreviation
states=hashmap.new()
hashmap.set(states,'oregan','or')
hashmap.set(states,'florida','fl')
hashmap.set(states,'california','ca')
hashmap.set(states,'new york','ny')
hashmap.set(states,'michigan','mi')

#create a basic set of states and some cities in them
cities=hashmap.new()
hashmap.set(cities,'ca','san francisco')
hashmap.set(cities,'mi','detroit')
hashmap.set(cities,'fl','jacksonville')

#add more cities
hashmap.set(cities,'ny','new york')
hashmap.set(cities,'or','portland')

#print out some cities
print '-'*10
print"ny state has %s"%hashmap.get(cities,'ny')
print"or state has %s"%hashmap.get(cities,'or')
#print some states
print'-'*10
print"michigan's abbreviation is %s"%hashmap.get(states,'michigan')
print"florida's abbreviation is %s"%hashmap.get(states,'florida')

#do it by using the state then cities dict
print'-'*10
print"michigan has:%s"%hashmap.get(cities,hashmap.get(states,'michigan'))
print"florida has :%s"%hashmap.get(cities,hashmap.get(states,'florida'))
#print every city in state
print'-'*10
hashmap.list(states)

#print every city in state
print'-'*10
hashmap.list(cities)

print'-'*10
state=hashmap.get(states,'texas')

if not state:
    print"sorry,no texas"

city=hashmap.get(cities, 'tx','does not exist')
print"the city for the state 'tx'is %s"%city
