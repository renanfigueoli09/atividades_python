
def max_value(value):
    nums = [i for i in value.values() if isinstance(i, (int, float))]

    if len(nums) == len(value):

        if nums:
            max_value = max(nums)

            return [max_value]
    
    return []

ex_01 = {'a': 10, 'b': -5, 'c': 20.5, 'd': -7.3}
print(max_value(ex_01))

ex_02 = {'x': 0, 'y': 0.0, 'z': 0.0, 'w': 0.0001}
print(max_value(ex_02)) 

ex_03 = {'nome': 'João', 'idade': 30, 'altura': 1.75, 'peso': '75 kg'}
print(max_value(ex_03)) 

ex_04 = {'a': 3.14, 'b': 2.71, 'c': 3.14, 'd': 1.61}
print(max_value(ex_04)) 
