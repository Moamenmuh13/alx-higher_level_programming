#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length  # Initialize the result list with zeros

    for i in range(list_length):
        try:
            element1 = my_list_1[i] if i < len(my_list_1) else 0
            element2 = my_list_2[i] if i < len(my_list_2) else 0
            result[i] = element1 / element2
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            if i < list_length - 1:
                print()

    return result
