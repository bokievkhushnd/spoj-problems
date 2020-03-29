t=int(input())
for n in range(t):
    inp=input().split()
    l,c=[int(i) for i in inp]
    def top_bot():
        l=['*' for i in range(c)]
        #for _ in range(c):
        print("".join(l))
    if l==1:
        top_bot()
        for i in range(l-2):
            print("*",end="")
            if c==1:
                print('\n')
                continue
            else:
                for k in range(c-2):
                    print(".",end="")
                print("*",end="\n")
                #print("\n")
    else:
        top_bot()
        for i in range(l-2):
            print("*",end="")
            if c==1:
                print('\n')
                continue
            else:
                for k in range(c-2):
                    print(".",end="")
                print("*",end="\n")
                #print("\n")
        top_bot()
