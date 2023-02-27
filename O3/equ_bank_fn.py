from random import randint
def eq_to_text(nums):
    p0 = make_x_part(nums[0])
    p1 = make_c_part(nums[1])
    p2 = make_x_part(nums[2])
    p3 = make_c_part(nums[3])
    return p0 + p1 + " = " + p2 + p3

def make_x_part(number):   
    x_part = "-" if number < 0 else ""
    x_part += "" if abs(number) == 1 else str(abs(number))
    x_part += "x"
    return x_part

def make_c_part(number):   
    sign = " + " if number > 0 else " - "
    return sign + str(abs(number))
    
def ok_equation(nums):
    if min(nums) == 0 or nums[0] == nums[2] or nums[1] == nums[3]:
        return False
    return True

def make_eq():
    eq = [0] * 4
    ok_eq = False
    while not ok_eq:
        for i in range(len[eq]):
            eq[i] = randint(-9,9)
        if ok_equation(eq):
            ok_eq = True
    return eq
    


def main():
    
    print(eq_to_text([-3,+5,-3,+5]))
    print(ok_equation([-3,+5,-2,+5]))
    print(make_eq()


main()