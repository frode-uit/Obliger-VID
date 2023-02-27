#USCapitals
import os

ASK_CHOICE = 1
QUIT_CHOICE = 2
capitals = {}
def main():
    try:
        capitals_file_name = "O1/USCapitals.txt"
        capitals_file = open(capitals_file_name, "r")
        for line in capitals_file:
            key_and_val = [x.strip() for x in line.split(sep=',')]
            capitals[key_and_val[0]] = key_and_val[1]
        capitals_file.close()
        
            
        choice = 0
        while choice != QUIT_CHOICE:
            display_menu()
            choice = int(input('Enter your choice: '))
            if choice == QUIT_CHOICE:
                break

            elif choice == ASK_CHOICE:
                state = input("Please enter state name: ")
                if state in capitals:
                    print(f'The capital of {state} is {capitals[state]}')
                else:
                    print("no such state")    
            else:
                print('Error: invalid selection.\n')

    except ValueError as ex:
        print(f'\nException: {ex}. Try again.')
        main()

def display_menu():
    print('\n        MENU')
    print('1) Ask for capital in state')
    print('2) Quit')     

if __name__ == '__main__':
    main()