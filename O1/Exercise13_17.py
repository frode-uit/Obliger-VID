import urllib.request

boyNames = []
girlNames = []
    
def readNames():
    for i in range(0, 10):
        if i == 9:
            filename = "babynamesranking2010.txt"
        else:
            filename = "babynamesranking200" + str(i + 1) + ".txt"
      
        boyNames.append([])
        girlNames.append([])
        inputFile = urllib.request.urlopen(
            "https://liveexample.pearsoncmg.com/data/" + filename)
        for line in inputFile:
            items = line.split()
            boyNames[i].append(items[1].decode())
            girlNames[i].append(items[3].decode())

def search(names, year, name):
    for i in range(0, 1000):
        if names[year - 2001][i] == name:
            return i
        
    return -1
      
def main():
    readNames()
    year = int(input("Enter the year: "))
    gender = input("Enter the gender: ")
    name = input("Enter the name: ")
     
    if gender == 'M':
        index = search(boyNames, year, name)
        if index >= 0:
            print("Boy name " + name + " is ranked #" + 
                str(index + 1) + " in year " + str(year))
        else:
            print("Boy name " + name + " is not ranked in year " 
                + str(year))
    else:
        index = search(girlNames, year, name)
        if index >= 0:
            print("Girl name " + name + " is ranked #" + 
                str(index + 1) + " in year " + str(year))
        else:
            print("Girl name " + name + " is not ranked in year " + 
                str(year))
    
main()