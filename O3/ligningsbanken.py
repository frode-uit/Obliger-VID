def main():

    tests = make_test(['Marte', 'Silje', 'Fredrik'], 5)
    ask_questions(tests)
    print(tests)

def make_x(num):
    if num == 1:
        return "x"
    elif num == -1:
        return "-x"
    else:
        return str(num) + "x"

def make_c(num):
    if num < 0:
        return " - " + str(abs(num))
    else:
        return " + " + str(abs(num))

def eq2text(L):
    l_side = make_x(L[0]) + make_c(L[1])
    h_side = make_x(L[2]) + make_c(L[3])
    return l_side + " = " + h_side 

def ok(L):
    if 0 in L:
        return False
    elif L[0] == L[2]:
        return False
    elif L[1] == L[3]:
        return False
    else:
        return True

def make_eq():
    from random import randint
    done = False
    while not done:
        eq = []
        for i in range(4):
            eq.append(randint(-9,9))
        if ok(eq):
            done = True
    return eq

def make_eqs(n):
    eq_list = []
    count = 0
    while count < n:
        eq = make_eq()
        if (eq not in eq_list and
            eq[2:] + eq[:2] not in eq_list):
                eq_list.append(eq)
                count +=1
    return eq_list

def make_test(students, n):
    tests = {}
    for stud in students:
        tests[stud] = make_eqs(n)
    return tests

def ask_questions(dict):
    ok_name =False
    while not ok_name:
        name = input("Enter your name: ")
        if name in dict:
            ok_name = True
    print("Please solve this equations: ")
    ch = "a"
    for eqs in dict[name]:
        print(f'{ch}) {eq2text(eqs)}')
        answer_ok = False
        while not answer_ok:
            try:
                ans = input("x = ")
                ans = float(ans.replace(',', '.'))
                answer_ok = True
            except:
                print("Invalid input ")
        eqs.append(ans)
        ch = chr(ord(ch) + 1)



main()