def get_odd_numbers(any_list):
    result = []
    for num in any_list:
        if num % 2 == 0:
            result.append(num)
    
    return result

print(get_odd_numbers([1,2,3,4,5]))

