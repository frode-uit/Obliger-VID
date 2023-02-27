
def main():
    filename = input("Enter a filename: ")
    oldString = input("Enter the old string to replace: ")
    newString = input("Enter the new string to replace the old with: ")
    replace(filename, oldString,newString)

def replace(file, old, new):
    lines = []
    with open(file) as inputFile:
        for line in inputFile:
            lines.append(line.replace(old, new))
    
    with open(file, "w") as outputFile:
        for line in lines:
            outputFile.write(line)

main()