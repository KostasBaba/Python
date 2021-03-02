x = int(input(""))
n1, n2 = 0, 1
count = 0

while count < x:
    y = n1 + n2
    n1 = n2
    n2 = y
    count += 1
r = 0

if n1 > 1:
    for i in range(2,n1) :
        if (n1 % i) == 0:
            print("Ο", x,"ος όρος είναι ο", n1, "και δεν είναι πρώτος" )
            break
        else:
            print("Ο", x,"ος όρος είναι ο", n1, "και είναι πρώτος" )
            break
else:
            print("Ο", x,"ος όρος είναι ο", n1, "και είναι πρώτος" )
