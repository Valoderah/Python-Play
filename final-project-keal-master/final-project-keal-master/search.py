
# r=open("test1.txt","r")

d = dict()

with open("test1.txt") as fp:
    line = fp.readline()
    while line:
        t = line.strip('\n')
        t = t.split(':')
        # print('%s, %s' % (t[0], t[1]))
        d[t[0]] = "919"+t[1]
        line = fp.readline()

while(True):
    n = input("Do you have name(n) or 919(9)? (q to quit)")
    if(n == "q"):
        break
    elif (n=="n"):
        r = input("Enter name of 919 you are looking for: ")
        if r in d:
            print("919#: ", d[r])
        else:
            print("This name does not exist")
    else:
        r = input("Enter 919# of name you are looking for: ")
        try:
            print(list(d.keys())[list(d.values()).index(r)])
        except:
            print("This 919# does not exist")