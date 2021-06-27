with open("1.txt", encoding="UTF-8") as file:
    number_str_1 = 0
    for line in file:
        number_str_1 += 1
    # print(number_str_1)

with open("2.txt", encoding="UTF-8") as file:
    number_str_2 = 0
    for line in file:
        number_str_2 += 1
    # print(number_str_2)

with open("3.txt", encoding="UTF-8") as file:
    number_str_3 = 0
    for line in file:
        number_str_3 += 1
    # print(number_str_3)

def list_length_min(a, b, c):
    if number_str_1 < number_str_2 and number_str_1 < number_str_3:
        return (a)
    elif number_str_2 < number_str_1 and number_str_2 < number_str_3:
        return (b)
    else:
        return (c)

def list_length_average(a, b, c):
    if number_str_1 > number_str_2 and number_str_1 < number_str_3:
        return (a)
    elif number_str_2 > number_str_1 and number_str_2 < number_str_3:
        return (b)
    else:
        return (c)

def list_length_max(a, b, c):
    if number_str_1 > number_str_2 and number_str_1 > number_str_3:
        return (a)
    elif number_str_2 > number_str_1 and number_str_2 > number_str_3:
        return (b)
    else:
        return (c)

list_length_min("1.txt", "2.txt", "3.txt")
list_length_average("1.txt", "2.txt", "3.txt")
list_length_max("1.txt", "2.txt", "3.txt")

with open("hw.txt", 'w', encoding="UTF-8") as document:
    document.write(f'{list_length_min("1.txt", "2.txt", "3.txt")}\n')
    with open(list_length_min("1.txt", "2.txt", "3.txt"), encoding="UTF-8") as file:
        number_str = 0
        for line in file:
            number_str += 1
        document.write(f'{number_str}\n')
    with open(list_length_min("1.txt", "2.txt", "3.txt"), encoding="UTF-8") as file:
        document.write(f'{file.read()}\n')

with open("hw.txt", 'a', encoding="UTF-8") as document:
    document.write(f'{list_length_average("1.txt", "2.txt", "3.txt")}\n')
    with open(list_length_average("1.txt", "2.txt", "3.txt"), encoding="UTF-8") as file:
        number_str = 0
        for line in file:
            number_str += 1
        document.write(f'{number_str}\n')
    with open(list_length_average("1.txt", "2.txt", "3.txt"), encoding="UTF-8") as file:
        document.write(f'{file.read()}\n')

with open("hw.txt", 'a', encoding="UTF-8") as document:
    document.write(f'{list_length_max("1.txt", "2.txt", "3.txt")}\n')
    with open(list_length_max("1.txt", "2.txt", "3.txt"), encoding="UTF-8") as file:
        number_str = 0
        for line in file:
            number_str += 1
        document.write(f'{number_str}\n')
    with open(list_length_max("1.txt", "2.txt", "3.txt"), encoding="UTF-8") as file:
        document.write(f'{file.read()}\n')