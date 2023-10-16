def most_frequent_number(value):
    nums = [i for i in value if isinstance(i, (int, float))]
    
    if len(nums) == len(value) and nums:
        count_numbers = {}
        
        for num in nums:
            if num in count_numbers:

                count_numbers[num] += 1
            else:

                count_numbers[num] = 1
        
        numero_mais_frequente = max(count_numbers, key=count_numbers.get)
        
        return numero_mais_frequente
    else:
        return -345

ex_01 = [1,2, 3, 4, 4, 4,2, 13, 7, 10, 80, 8, 7,1, 4, 12, 4, 11, 9, 4, 8, 1]
print(most_frequent_number(ex_01)) 

ex_02 = [10, 20, 'teste', 10, 20, [], 10.0, 30,70, 80, 71]
print(most_frequent_number(ex_02)) 

ex_03 = []
print(most_frequent_number(ex_03)) 