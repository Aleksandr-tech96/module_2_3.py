my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while len(my_list) > i: # True
    number = my_list[i]
    if number < 0:
        break

    if number == 0:
        i += 1
        continue

    print(number)

    i += 1