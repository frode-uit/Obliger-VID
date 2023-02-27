# this code will find a convex hull 

from math import atan2,degrees,dist
initial_points = []
points = []
low_x = 0
low_y = 0
 
# code to detect if point p2 is on line, to the left or to the right of a line from p0 to p1
def which_side(x0,y0,x1,y1,x2,y2)->float: # 0, -> same line, > 0, -> p2 on the left of p1, < 0 p2 on right
    return (x1 - x0)*(y2 - y0)-(x2 - x0)*(y1 - y0)

def length_between_points(x1, y1):
    return dist([low_x,low_y],[x1,y1])

def getRightmostLowestIndex(p):
    rightMostIndex = 0;
    rightMostX = p[0][0];
    rightMostY = p[0][1];
    
    for i in range(1, len(p)):
        if rightMostY > p[i][1]:
            rightMostY = p[i][1]
            rightMostX = p[i][0]
            rightMostIndex = i
        elif rightMostY == p[i][1] and rightMostX < p[i][0]:
            rightMostX = p[i][0]
            rightMostIndex = i   
    
    return rightMostIndex

def get_angle_of_line_between_two_points(x0, y0, x1, y1)->float:
    xDiff = x1 - x0
    yDiff = y1 - y0
    return degrees(atan2(yDiff, xDiff))

def get_sorted_on_angles(points):
    if len(points) < 3:
        return points
    index_of_rl = getRightmostLowestIndex(points)
    low_x = points[index_of_rl][0]
    low_y = points[index_of_rl][1]
    points.pop(index_of_rl) # will store back after sorting
    points_and_angles = [[x,y,0] for x, y in points]    
    for i in range(len(points_and_angles)):
        points_and_angles[i][2] = get_angle_of_line_between_two_points(points[0][0],points[0][1],points[i][0],points[i][1]) # find angle
    points_and_angles.sort(key = lambda t:t[2]) # sort on angle
    discard_closest_with_same_angle(points_and_angles)
    points = [[x,y] for x,y,z in points_and_angles]
    points.insert(0,[low_x,low_y])
    return points

def discard_closest_with_same_angle(points):
    set_of_angles = set()
    for i in range(0, len(points)):
        if points[i][2] not in set_of_angles:
            set_of_angles.add(points[i][2])
        else:
            for j in range(i,len(points)):
                if (length_between_points(points[i][0],points[i][1]) > \
                    length_between_points(points[j][0],points[j][1])):
                        points[j][2] = None
    for item in points:
        if item[2] == None:
            points.remove(item)
            
   

def get_convex_hull(points):
    if len(points) < 3:
        return points
   
    stack = [points[0], points[1], points[2]]
    
    i = 3
    while i < len(points):
        t1 = stack[len(stack) - 1]
        t2 = stack[len(stack) - 2]
        if which_side(t2[0],t2[1],t1[0],t1[1],points[i][0],points[i][1])<= 0:
            stack.pop()
        else:
            stack.append(points[i])
            i += 1
    return stack
   
def find_convex_hull(points):
    get_sorted_on_angles(points)
    return get_convex_hull(points)
    
    
       
# get points from keyboard or file
def get_points(points):
    choice = input("Read from file or from keyboard (f/k) ? ")
    if choice.upper() == 'F':
        try:
            filename = input("File name : ")
            with open(filename) as f:
                i = 0
                for line in f:
                    x_y_pair = [float(n) for n in line.split()] # list of str to list of float x,y
                    points.append(x_y_pair)
        except IOError:
            print("Error : cannot find file")
            quit()        
    elif choice.upper() == 'K':    
        noof_points = int(input("Enter number of  x y pairs : "))
        for i in range(noof_points):
            x_y_pair_as_str = input(f'Enter point {i + 1}, two float numbers with space as delimiter : ')
            x_y_pair = [float(n) for n in x_y_pair_as_str.split()] # list of str to list of int x,y
            points.append(x_y_pair)
    else:
        print("Illegal choice")
        quit()
    
    #initial_points = points[:]

def main():
    get_points(points)
    find_convex_hull(points)
    #print(f'The initial points : {initial_points}')
    print(f'The convex hull : {points}')
    
if __name__ == '__main__':
    main()