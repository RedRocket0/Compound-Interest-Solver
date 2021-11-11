import math
#Compound Interest Solver

def FandCSolver():
    p = float(input("Principal Amt: "))
    r = float(input("Rate(in decimal): "))
    n = float(input("Number of times compounded: "))
    t = float(input("Time(in years): "))

    a = (1 + r/n)
    b = n * t
    c = a ** b
    f = p * c

    print("Future Value: " + str(f))
    ic = f - p
    print("Compound Interest: " + str(ic))

def PSolver():
    f = float(input("Future Value: "))
    r = float(input("Rate(in decimal): "))
    n = float(input("Number of times compounded: "))
    t = float(input("Time(in years): "))

    a = (1 + r/n)
    b = (n * t)
    c = a ** b
    p = f/c

    print("Principal Amount: " + str(p))

def RSolver():
    n = float(input("Number of times compounded: "))
    f = float(input("Future Value: "))
    p = float(input("Principal Amount: "))
    t = float(input("Time(in years): "))

    a = n * t
    b = 1/a
    c = f/p
    d = c ** b - 1
    r = d * n * 100

    print("Rate: " + str(r) + "%")

def TSolver():
    f = float(input("Future Value: "))
    p = float(input("Principal Amount: "))
    n = float(input("Number of times compounded: "))
    r = float(input("Rate(in decimal): "))

    a = math.log(f) - math.log(p)
    b = math.log(1 + r/n)
    c = n * b
    t = a/c

    print("Time: " + str(t) + " years")

print("What is/are the missing values?")
answer = input("future value('f' only), principal('p only), rate('r' only), time('t' only): ")

if (answer == 'f'):
    FandCSolver()

elif (answer == 'p'):
    PSolver()

elif (answer == 'r'):
    RSolver()

elif (answer == 't'):
    TSolver()

else:
    print("Invalid input!")
