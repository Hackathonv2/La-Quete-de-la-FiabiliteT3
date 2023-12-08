import sys

def calcul(string1, string2):
    f1 = int(string1[1])
    p1 = int(string1[2])
    r1 = int(string1[3])
    result1 = string1[0]

    f2 = int(string2[1])
    p2 = int(string2[2])
    r2 = int(string2[3])
    result2 = string2[0]

    if 1 <= r1 <= 20 and 1 <= p1 <= 20 and 1 <= f1 <= 20:
        if 1 <= r2 <= 20 and 1 <= p2 <= 20 and 1 <= f2 <= 20:
            res1 = (r1 + p1) * f1
            res2 = (r2 + p2) * f2
        else:
            return 84
    else:
        return 84

    if res1 > res2:
        return result2
    elif res2 > res1:
        return result1
    else:
        return 0

if __name__ == "__main__":
    content = sys.stdin.read().splitlines()
    string1 = content[0].split()
    string2 = content[1].split()
    print(calcul(string1, string2))
