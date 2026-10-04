c0 = int(input("Please enter a number to participate in Collatz's Hypothesis: "))
count = 0

while c0 != 1:
    count += 1
    
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 = (c0 * 3) + 1
    
    print(int(c0))
    
    
print("Count: ", count)
