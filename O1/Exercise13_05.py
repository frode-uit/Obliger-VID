def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a filename: ").strip()

    # Open files for input 
    inputFile = open(f1, "r")
    
    s = inputFile.read() # Read all from the file
    
    oldString = input("Enter the old string to be replaced: ").strip()
    newString = input("Enter the new string to replace the old string: ").strip()
    
    newS = s.replace(oldString, newString)
    
    inputFile.close()  # Close the input file
    outputFile = open(f1, "w")
    
    print(newS, file = outputFile, end = "") # Write to the file
    print("Done") 

    outputFile.close() # Close the output file

main()
