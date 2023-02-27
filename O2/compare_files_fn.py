def main():
    # Prompt the user to enter a file
    filename1 = input("Enter filename of the first file: ").strip()
    inputFile1 = open(filename1, "r") # Open the file
    filename2 = input("Enter filename of the second file: ").strip()
    inputFile2 = open(filename2, "r") # Open the file

    words1 = {}
    processFile(inputFile1, words1)
    inputFile1.close() 
    
    words2 = {}
    processFile(inputFile2, words2)
    inputFile2.close()
    # Show number of unique words in both files
    print(f'Number of unique words in file 1 : {len(words1)} , file 2 : {len(words2)}')
    
    # Show the unique words in both files
    print(f'The unique words in file 1 are :')
    showWords(words1)
    print(f'The unique words in file 2 are :')
    showWords(words2)
    
    #pairs = list(wordCounts.items()) # Get pairs from the dictionary   

    #items = [[x, y] for (y, x) in pairs] # Reverse pairs in the list

    #items.sort() # Sort pairs in items

    #for i in range(len(items) - 1, len(items) - 11, -1):
    #    print(items[i][1] + "\t" + str(items[i][0]))
  
# Count each word in the line
def processFile(inputfile, set_of_words): 
    for line in inputfile:        
        line = replacePunctuations(line.lower()) # Replace punctuations with space
        words = line.split() # Get words from each line
        for word in words:
            if word not in set_of_words:
                words.add(set_of_words)    

# Replace punctuations in the line with space
def replacePunctuations(line):
    for ch in line:
        if ch in '~@#$%^&*()_-+=~"<>?/,.;!{}[]|':
            line = line.replace(ch, " ")

    return line

def showWords(dict):
    words = 0
    for key in dict:
        print(key,end=' ')
        words += 1
        if words % 10 == 0:
            print()
    print()    

main()