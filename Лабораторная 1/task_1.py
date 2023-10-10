numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_missing_item = 4

sum_of_numbers = sum(numbers[:index_missing_item]) + sum(numbers[index_missing_item+1:])
count_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers / count_of_numbers

numbers[index_missing_item] = average_of_numbers
print("Измененный список:", numbers)

"""
изначальное решение задачи отличалось тем, что вместо index_missing_item = 4, было написано 
number[4] = 0. 
вместо sum_of_numbers = sum(numbers[:index_missing_item]) + sum(numbers[index_missing_item+1:])
было написано sum_numbers = sum(numbers)
на этом основывалось дальнейшее создание кода программы
"""