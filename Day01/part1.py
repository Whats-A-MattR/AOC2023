
with open("input.txt") as f:
    lines = f.readlines()
    print(f'{len(lines)} \n')

    total = 0

    for x in lines:
        print(f'{x} \n')
        num = [i for i in x if i.isdigit() == True]
        out = 0 
        first_and_last = [num[0], num[-1]]
        new_num = ''.join(first_and_last)
        out = int(new_num)
        total += out
        print(f'numbers in string: {num}, total this step: {out} running total: {total} \n')