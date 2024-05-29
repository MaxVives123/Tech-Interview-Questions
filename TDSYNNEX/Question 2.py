def sort_string(shakespeare):
    #I do it like this in order to not use libraries to remove the punctuation.
    punctuation = [',', '.', '!', '?', ';', ':', "'", '"']  
    for p in punctuation:
        shakespeare = shakespeare.replace(p, '')
    
    words = shakespeare.split()
    
    words = [word.lower() for word in words]
    
    # Here I use the function I created on the first exercice adapted to this one
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
    words_sorted = quick_sort(words)
    
    string_sorted = ' '.join(words_sorted)
    
    return string_sorted

shakespeare = 'All the world is a stage, and all the men and women merely players. They have their exits and their entrances, And one man in his time plays many parts.'
sorted_string = sort_string(shakespeare)
print(sorted_string)
