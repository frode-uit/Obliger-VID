# fn
# Liang sitt løsningsforslag bruker read (leser alt i en klump)
# Går det bra med store filer?
# Denne koden leser linje for linje, skriver til temporær fil
# og renamer (os.replace) til original
import os
def main():
    while True:
        try:
            fileName = input("Filnavn:").strip()
            inFile = open(fileName,"r")
            break
        except IOError:
            print(f'File {fileName} does not exist, try again')
    existingWord = input("Ord som skal erstattes:").strip()
    newWord = input("..erstatt med:").strip()
    
    outFile = open("temp.txt","w")
    for line in inFile:
        newLine = line.replace(existingWord, newWord)
        outFile.write(newLine)
    inFile.close()
    outFile.close()
    os.replace("temp.txt",fileName)

main()