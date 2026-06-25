# ---------------------------------------------------------

# Variable scope - where a variable is visible and accessible
# Scope resolution = (LEGB) L > E > G > B - order

def func1(): # Local in func
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

def func1(): # Enclosed in func
    x = 1 # if x = 2 is removed then x = 1

    def func2(): # Local in func
        x = 2
        print(x)
    func2()

func1()

# Global
def func1():
    print(x)

def func2():
    print(x)

x = 3

func1()
func2()

# Built in
from math import e

def func1():
    print(e)

e = 3
func1()

# ---------------------------------------------------------

# if __name__ == "__main__":

# def main():
#     pass

# if __name__ == "__main__":
#     main()

# ---------------------------------------------------------
