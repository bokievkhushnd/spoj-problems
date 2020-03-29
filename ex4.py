t = int(input())
for n in range(t):
    inp = input().split()
    l, c = [int(i) for i in inp]
    for i in range(1, l+1):
        if i % 2 == 0:
            print(".", end="")
        else:
            print("*", end="")
        if c == 1:
            print("\n")
            continue
        else:
            for j in range(i+1, c+i):

                if j % 2 == 0:
                    print(".", end="")
                else:
                    print("*", end="")
        print("\n")
