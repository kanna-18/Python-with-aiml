def analyze_list(lst):
    sum_val = 0
    even_count = 0
    odd_count = 0

    for num in lst:
        sum_val += num
        
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    average = sum_val / len(lst) if len(lst) > 0 else 0

    return sum_val, average, even_count, odd_count
    
numbers = [1, 2, 3, 4, 5, 6]

result = analyze_list(numbers)

print("Sum:", result[0])
print("Average:", result[1])
print("Even count:", result[2])
print("Odd count:", result[3])
