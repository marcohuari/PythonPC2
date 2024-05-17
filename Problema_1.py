
flag_res = 0
i = 1

for n in range(1500,2700):
    if n%7 == 0 and n%5 == 0:
        flag_res = 1
    else:
        flag_res = 0
    if flag_res == 1:
        print(f"{i}.{n}")
        i = i + 1