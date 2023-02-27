#Geometry: Gift-wrapping algorithm for finding a convex hull

def rightmostBottom(S):

    H0 = max(S, key = lambda y:y[1]) 
    for point in S:
        if point[0] > H0[0] and point[1] == H0[1]:
            H0 = point

    return H0


def getDirection(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3
    direction = (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)
    
    if direction > 0:
        return 1
    elif direction < 0:
        return -1
    else:
        return 0


def distance(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    dist = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

    return dist


def getConvexHull(S):
    H0 = rightmostBottom(S)
    H = []

    while True:
        H.append(H0)
        T1 = S[0]
        for point in S:
            d = getDirection(H0, T1, point)
            if T1 == H0 or d == 1 or (d == 0 and distance(H0, point) > distance(H0, T1)):
                T1 = point
        H0 = T1
        if H0 == H[0]:
            break

    return H

    #Interessant med unødvendig tillegginfo av meg:

    #I boken til Liang beskrives algoritmen med å starte "rightmost lowest point", 
    # og derfor laget jeg funksjonen rightmostBottom og starter med denne.
    #I mange andre eksempler så starter Jarvis March algoritmen(som dette er)
    #helt til venstre, og jeg ville da simpelt ha brukt denne linjen i stede for 
    #egen funksjon for H0, men dette spiller egentlig ingen rolle og koden funker like bra uansett: 
    #H0 = min(S)
    #I de fleste andre tilfeller så søkes det motsatt vei også, og dette kunne vært gjort med 
    #å bytte d == -1 i linje 41 til d == 1. Dette spiller da egentlig ingen rolle heller og koden funker like
    #bra uansett hvordan vei man går. 
    #Jeg har fulgt akkurat hvordan Liang skrev.