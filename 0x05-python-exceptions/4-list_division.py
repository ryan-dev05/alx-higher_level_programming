#!/sur/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                val_1 = my_list_1[i] if i < len(my_list_1) else 0
                val_2 = my_list_2[i] if i < len(my_list_2) else 1
                division_result = val_1 / val_2
                result.append(division_result)
            except TypeError:
                print("wrong type")
                result.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
    except IndexError:
        print("out of range")

    return result
