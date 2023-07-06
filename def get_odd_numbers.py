def get_odd_numbers(any_list):
    result = []
    for num in any_list:
        if num % 2 == 0:
            result.append(num)
    
    return result

def add_num(a, b):
    return a + b
print(get_odd_numbers([1,2,3,4,5]))


#123