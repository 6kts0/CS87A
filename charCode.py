S = 'W'
P = 'python'

# ord returns the binary code of a char in memory
print(ord('O'))

# You can also do math with ord
print(ord(S) + 10) 

# Looping through a string to return each binary digits
def main():
    global P
    stk = []
    for i in P:
        if i:
            stk.append(ord(i))
        if i == 'n':
            print(stk)

if __name__ == '__main__':
    main()
