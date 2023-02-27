from fileinput import close

f = open("capitals.txt")

dic = {}
for line in f:
    state, capital = line.split(",")
    capital = capital.rstrip("\n")
    dic.update(state:capital)

state_search = input("Enter the name of a state: ")
found = False

for state in dic.keys():
    if state == state_search:
        found = True
        capital = dic[state]

if found:
    print(capital, "is the capital of", state_search)
else:
    print(The state ", state_search, " was not in the list")

f.close