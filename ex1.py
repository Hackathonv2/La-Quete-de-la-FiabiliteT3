import sys
#cat input.txt | python3 ex1.py

def first_string(string):
    i = 0
    first = []
    while (string[i] != '\n'):
        first.append(string[i])
        i += 1
    return first

def second_string(string):
    i = 0
    second = []
    while (string[i] != '\n'):
        i += 1
    i += 1
    while (i < len(string)):
        second.append(string[i])
        i += 1
    return second

def calcul(string1, string2):
    f1 = string1[4]
    p1 = string1[6]
    r1 = string1[8]

    f2 = string2[4]
    p2 = string2[6]
    r2 = string2[8]
    if r1 >= 1 and r1 <= 20 and p1 >= 1 and p1 <= 20 and f1 >= 1 and f1 <= 20:
        if r2 >= 1 and r2 <= 20 and p2 >= 1 and p2 <= 20 and f2 >= 1 and f2 <= 20:
            res1 = (r1 + p1) * f1
            res2 = (r2 + p2) * f2
        else:
            return 84
    else:
        return 84
    if (res1 > res2):
        return res2
    if (res2 > res1):
        return res1


if __name__ == "__main__":
    content = sys.stdin.read()
    string1 = first_string(content)
    string2 = second_string(content)
    print(content)
    print(string1)
    print("---------------------------------------------")
    print(string2)
    print("---------------------------------------------")
    print(calcul(string1, string2))