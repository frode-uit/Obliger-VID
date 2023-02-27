def reverse(value):
    if value // 10 == 0:
        print(value)
        return
    print( value % 10,end="")
    reverse(value // 10)

def main():
    value = int(input("Gi inn et tall:"))
    reverse(value)

main()