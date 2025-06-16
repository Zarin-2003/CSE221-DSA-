
def mod_exp(a, b, mod):
    result = 1
    while b > 0:
        if b % 2 == 1: #if odd, suppose 2^5, then 2*2^4. 
            result = (result * a) % mod  #that 2 comes here
        a = (a * a) % mod #if even, like 2^4. then (2^2)^4/2
        b //= 2  #2^2 happens in 8th line and 4/2 happens here
    return result

a,b=input().split()
a,b=int(a),int(b)
result=mod_exp(a,b,107)
print(result)

