#Exercise 1
#numbers_disordered = [ 4, 1, 6, 43, 16, 88, 2, 100]
#Create a function that returns as short as possible a list of ordered numbers. The shorter the better. (Tip: now you have to create the algorithm) DON’T USE function SORT

def sort_numbers(numbers_disordered):
    if len(numbers_disordered) <= 1:
        return numbers_disordered
    pivot = numbers_disordered[len(numbers_disordered) // 2]
    left = [x for x in numbers_disordered if x < pivot]
    middle = [x for x in numbers_disordered if x == pivot]
    right = [x for x in numbers_disordered if x > pivot]
    return sort_numbers(left) + middle + sort_numbers(right)
    
numbers_disordered = [4, 1, 6, 43, 16, 88, 2, 100]
sorted_numbers = sort_numbers(numbers_disordered)
print(sorted_numbers)
