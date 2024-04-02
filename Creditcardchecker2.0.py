for i in range(len(list)):
    number = list[i]
    if i == 0 and number > list[i + 1]:
        print(number * "*", "Peak")
    elif 0 < i < len(list) - 1 and list[i - 1] < number > list[i + 1]:
        print(number * "*", "Peak")
    elif 0 < i < len(list) - 1 and list[i - 1] <= number >= list[i + 2]:
        print(number * "*", "Peak")
    elif i == len(list) - 1 and number > list[i - 1]:
        print(number * "*", "Peak")
    else:
        print(number * "*")