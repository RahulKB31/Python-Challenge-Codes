<<<<<<< HEAD
#650

'''
Execute a string of code in Python
'''

# Use exec() function

def exec_code():
    LOC = """
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact
print(factorail(5))
"""
    exec(LOC)

exec_code()

############################################################################################################

#651

'''
Using eval()
'''

code = '6+5'
result = eval(code)
print(result)

###########################################################################################################

#652

code = '"hello" + "world"'
result = eval(code)
print(result)

code = '["a","b","c"][1]'
result = eval(code)
print(result)

################################################################################################################

#653

import types

code_string = "a = 6+5"
my_namespace = types.SimpleNamespace()
exec(code_string, my_namespace.__dict__)
print(my_namespace.a)

################################################################################################################





































































































=======
#650

'''
Execute a string of code in Python
'''

# Use exec() function

def exec_code():
    LOC = """
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact
print(factorail(5))
"""
    exec(LOC)

exec_code()

############################################################################################################

#651

'''
Using eval()
'''

code = '6+5'
result = eval(code)
print(result)

###########################################################################################################

#652

code = '"hello" + "world"'
result = eval(code)
print(result)

code = '["a","b","c"][1]'
result = eval(code)
print(result)

################################################################################################################

#653

import types

code_string = "a = 6+5"
my_namespace = types.SimpleNamespace()
exec(code_string, my_namespace.__dict__)
print(my_namespace.a)

################################################################################################################





































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
