i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{i}*{j}={i * j}\t",end='')
        j = j + 1
    i = i + 1
    print()