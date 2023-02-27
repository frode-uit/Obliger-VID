def main():
    fileIn = open(input('enter an input file name: '), 'r')
    content = fileIn.read().split()
    fileOut = open(input('enter an output file name: '), 'w')
    oldStr = input('enter the old string to alter: ')
    newStr = input('enter the new string to replace it with: ')

    for i in range(len(content)):
        content[i] = f'{content[i]}\n'
    for line in content:
        if line == f'{oldStr}\n':
            line = f'{newStr}\n'
            fileOut.write(line)
        else:
            fileOut.write(line)
    fileIn.close()
    fileOut.close()
    print('Done')

main()