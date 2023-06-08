num1 = 11
num2 = num1

# will point to the same memory
print(f'num1 = {num1} memory:{id(num1)} \nnum2 = {num2} memory:{id(num2)}')

# will be different here because integers are immutable, which means they cannot be changed
num2 = 22
print(f'num1 = {num1} memory:{id(num1)} \nnum2 = {num2} memory:{id(num2)}')


# Dictionaries
dict1 = {
    'value': 1
}
dict2 = dict1

# will point to the same address
print(f'dict1 = {dict1}')
print(f'dict2 = {dict2}')
print(f'dict1 in memory = {id(dict1)}')
print(f'dict2 in memory = {id(dict2)}')

# change value
dict2['value'] = 22

# will still point to the same address with an updated value
print(f'dict1 = {dict1}')
print(f'dict2 = {dict2}')
print(f'dict1 in memory = {id(dict1)}')
print(f'dict2 in memory = {id(dict2)}')