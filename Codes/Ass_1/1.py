t=int(input())
if 1<=t<=100:
    for i in range(t):
        n=int(input())
        if -10**5<=n<=10**5:
            if n%2==0:
                print(f"{n} is an Even number.")
            else:
                print(f"{n} is an Odd number.")
        else:
            print("Invalid number")
else:
    print("Invalid")